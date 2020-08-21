from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import os.path

#################### USER CUSTOMIZE ###################################


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Users(AbstractBaseUser):

	GENDER = [
		('Male', 'Male'),
		('Female', 'Female'),
	]



	############### Fields ####################3
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	first_name				= models.CharField(max_length=30)
	last_name				= models.CharField(max_length=30)
	birthday				= models.DateField(blank=True, null=True)
	gender					= models.CharField(max_length=10, choices=GENDER , null=True, blank=True, default="Male")
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_online				= models.BooleanField(default=False)
	date_joined 			= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login 				= models.DateTimeField(verbose_name='last login', auto_now=True)
	first_login				= models.BooleanField(default=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()


	def save(self, *args, **kwargs):
		if not self.username:
			user = Users.objects.all().order_by('-pk').first()
			pk = user.pk + 1
			self.username = f'{self.first_name}{pk}'
		super(Users, self).save(*args, **kwargs)

	def __str__(self):
		return self.username



	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True





###################### PROFILE METHOD ########################

def profile_picture_upload(instance , filename):
	iconname , extension = os.path.splitext(filename)
	return f'profile/{instance.id}/picture/{iconname}.{extension}'

def profile_cover_upload(instance, filename):
	iconname , extension = os.path.splitext(filename)
	return f'profile/{instance.id}/cover/{iconname}.{extension}'

class Profile(models.Model):

	user                = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='profile')
	picture				= models.ImageField(upload_to=profile_picture_upload, default="user-default.png")
	cover				= models.ImageField(upload_to=profile_cover_upload, default="default-cover.jpg")
	bio					= models.TextField(max_length=300, blank=True, null=True)
	followers 			= models.ManyToManyField(Users, related_name='followers', default=None, blank=True)
	following 			= models.ManyToManyField(Users, related_name='following', default=None, blank=True)


	def __str__(self):
		return self.user.username


	@receiver(post_save, sender=Users)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
