from django.db import models

from accounts.models import Users

# Create your models here.




###################### Community METHOD ########################

def community_picture_upload(instance,filename):
    iconname , extension = filename.split('.')
    return f'community/{instance.id}/picture/{iconname}.{extension}'
def community_cover_upload(instance,filename):
    iconname , extension = filename.split('.')
    return f'community/{instance.id}/cover/{iconname}.{extension}'






class Community(models.Model):

    name        = models.CharField(max_length=100)
    bio         = models.TextField(max_length=255)
    picture     = models.ImageField(upload_to=community_picture_upload, default="default.jpg")
    cover       = models.ImageField(upload_to=community_cover_upload, default="default.jpg")
    admins      = models.ManyToManyField(Users, related_name='admin_community', default=None, blank=True)
    members     = models.ManyToManyField(Users, related_name='community', default=None, blank=True)

    def __str__(self):
        return str(self.id)