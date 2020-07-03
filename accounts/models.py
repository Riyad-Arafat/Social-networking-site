from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



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
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	first_name				= models.CharField(max_length=30)
	last_name				= models.CharField(max_length=30)
	birthday				= models.DateField(blank=True, null=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	date_joined 			= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login 				= models.DateTimeField(verbose_name='last login', auto_now=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()


	def save(self, *args, **kwargs):
		if not self.username:
			x = self.email
			i = 0
			m = ""
			while i < len(x):
				if x[i] == "@":
					break
				m += x[i]
				i += 1
			self.username = m
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

def profile_picture_upload(instance,filename):
	imgename , extention = filename.split('.')
	return f'profile/{instance.id}/picture/{imgename}.{extention}'
def profile_cover_upload(instance,filename):
	imgename , extention = filename.split('.')
	return f'profile/{instance.id}/cover/{imgename}.{extention}'

class Profile(models.Model):

	user                = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='profile')
	username			= models.CharField(max_length=30)
	first_name 			= models.CharField(max_length=30)
	last_name 			= models.CharField(max_length=30)
	picture				= models.ImageField(upload_to=profile_picture_upload,default="default.jpg")
	cover				= models.ImageField(upload_to=profile_cover_upload,default="default.jpg")
	bio					= models.TextField(max_length=150, blank=True, null=True)
	university			= models.CharField(max_length=30)
	faculty				= models.CharField(max_length=30)
	level				= models.CharField(max_length=30)
	nationality			= models.CharField(max_length=30)
	location			= models.CharField(max_length=30)


	@receiver(post_save, sender=Users)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(
				user=instance,
				username=instance.username,
				first_name=instance.first_name,
				last_name=instance.last_name,
			)
		else:
			profile = Profile.objects.get(user=instance)
			profile.username = instance.username
			profile.first_name = instance.first_name
			profile.last_name = instance.last_name
			profile.save()




	def __str__(self):
		return self.user.username



