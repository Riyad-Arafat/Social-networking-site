from django.db import models
from django.utils import timezone

from accounts.models import Users

from posts.models import Post
# Create your models here.



class Notification(models.Model):
    TYPE = [
        ('like', 'like'),
        ('comment', 'comment'),
        ('follow', 'follow'),
    ]


    type            = models.CharField(max_length=10, choices=TYPE, null=True, blank=True)
    user            = models.ForeignKey(Users, related_name='notification', on_delete=models.CASCADE, null=True, blank=True)
    sender          = models.ForeignKey(Users, related_name='note', on_delete=models.CASCADE, null=True, blank=True)
    post            = models.ForeignKey(Post,  related_name='notification', on_delete=models.CASCADE, null=True, blank=True)

    content         = models.TextField(max_length=100)
    readable        = models.BooleanField(default=False)
    all             = models.ManyToManyField(Users, related_name='notification_for_all', blank=True)

    created_at      = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.user.username



    def save(self, *args, **kwargs):
        if self.type == 'like':
            self.content = "liked to your post"

        elif self.type == 'comment':
            self.content = 'commented to your post'

        elif self.type == 'follow':
            self.content = 'followed you'

        super(Notification, self).save(*args, **kwargs)


