from django.db import models
from django.utils import timezone

from accounts.models import Users

from posts.models import Post
# Create your models here.



class Notification(models.Model):
    TYPE = [
        ('like', 'like'),
        ('comment', 'comment'),
        ('comment_like', 'comment_like'),
        ('reply', 'reply'),
        ('reply_like', 'reply_like'),
        ('follow', 'follow'),
    ]


    type            = models.CharField(max_length=30, choices=TYPE, null=True, blank=True)
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
            self.content = "Liked to your post"

        elif self.type == 'comment':
            self.content = 'Commented to your post'

        elif self.type == 'comment_like':
            self.content = 'Liked to your comment'

        elif self.type == 'reply':
            self.content = 'Replied to your comment'

        elif self.type == 'reply_like':
            self.content = 'Liked to your reply'

        elif self.type == 'follow':
            self.content = 'Followed you'

        super(Notification, self).save(*args, **kwargs)


