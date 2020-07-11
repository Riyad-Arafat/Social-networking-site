from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from accounts.models import Profile,Users

from urlextract import URLExtract

# Create your models here.


class Post(models.Model):
    author          = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    content         = RichTextField(blank=True, null=True)
    created_at      = models.DateTimeField(default=timezone.now)
    update_at       = models.DateTimeField(auto_now=True)
    viewers         = models.ManyToManyField(Users, related_name='viewed_posts', default=None, blank=True)

    def save(self, *args, **kwargs):

        extractor = URLExtract()
        urls = extractor.find_urls(self.content)
        x = self.content
        y = 0
        while y < len(urls):
            i = f'<a href="{urls[y]}">{urls[y]}</a>'
            if i not in self.content:
                self.content = x.replace(urls[y], f'<a href="{urls[y]}">{urls[y]}</a>')
            y += 1

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.author.username



class Comment(models.Model):
    author          = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    content         = models.TextField()
    created_at      = models.DateTimeField(default=timezone.now)
    update_at       = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.author.username
