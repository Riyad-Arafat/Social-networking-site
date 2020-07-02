from django.db import models
from django.utils import timezone
from accounts.models import Profile,Users
# Create your models here.


class Post(models.Model):
    author          = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    content         = models.TextField()
    created_at      = models.DateTimeField(default=timezone.now)
    update_at       = models.DateTimeField(auto_now=True)
    viewers         = models.ManyToManyField(Users,related_name='viewed_posts', blank=True, null=True)




    def __str__(self):
        return self.author.username