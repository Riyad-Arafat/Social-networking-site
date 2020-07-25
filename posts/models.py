import re
import os.path

from django.db import models
from django.utils import timezone

from accounts.models import Profile, Users
from community.models import Community
from ckeditor.fields import RichTextField

# Create your models here.


######### save post image #################
def post_image_upload(instance, filename):
    iconname , extension = os.path.splitext(filename)
    return f'profile/{instance.author.id}/posts/{iconname}.{extension}'


class Post(models.Model):
    author          = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    community       = models.ForeignKey(Community, on_delete=models.CASCADE, default=None, related_name='posts', blank=True, null=True)
    content         = RichTextField(blank=True, null=True)
    image           = models.ImageField(upload_to=post_image_upload, default=None, null=True, blank=True)
    created_at      = models.DateTimeField(default=timezone.now)
    update_at       = models.DateTimeField(auto_now=True)
    viewers         = models.ManyToManyField(Users, related_name='viewed_posts', default=None, blank=True)
    likes          = models.ManyToManyField(Users, related_name='liked_posts', default=None, blank=True)

    def save(self, *args, **kwargs):

        regex_url = '(http[s]?:\/\/[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        urls = re.findall(regex_url, self.content, re.MULTILINE)

        regex_hash_tag = '(#[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        hash_tag = re.findall(regex_hash_tag, self.content, re.MULTILINE)

        regex_mentions = '(@[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        mentions = re.findall(regex_mentions, self.content, re.MULTILINE)

        for url in urls:
            i = f'<a target="_blank" href="{url}">{url}</a>'
            if i not in self.content:
                self.content = self.content.replace(str(url), i)


        for tag in hash_tag:
            i = f'<a  class="hash-tag" href="#">{tag}</a>'
            if i not in self.content:
                self.content = self.content.replace(tag, i)

        for tag in mentions:
            i = f'<a href="{tag[1:]}">{tag[1:]}</a>'
            if i not in self.content:
                self.content = self.content.replace(tag, i)


        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.author.username






class Comment(models.Model):
    author          = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    content         = models.TextField()
    created_at      = models.DateTimeField(default=timezone.now)
    update_at       = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        regex_url = '(http[s]?:\/\/[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        urls = re.findall(regex_url, self.content, re.MULTILINE)

        regex_hash_tag = '(#[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        hash_tag = re.findall(regex_hash_tag, self.content, re.MULTILINE)

        regex_mentions = '(@[^"<\s]+)(?![^<>]*>|[^"]*?<\/a)'
        mentions = re.findall(regex_mentions, self.content, re.MULTILINE)

        for url in urls:
            i = f'<a target="_blank" href="{url}">{url}</a>'
            if i not in self.content:
                self.content = self.content.replace(str(url), i)


        for tag in hash_tag:
            i = f'<span class="hash-tag">{tag}</span>'
            if i not in self.content:
                self.content = self.content.replace(tag, i)

        for tag in mentions:
            i = f'<a href="{tag[1:]}">{tag[1:]}</a>'
            if i not in self.content:
                self.content = self.content.replace(tag, i)


        super(Comment, self).save(*args, **kwargs)



    def __str__(self):
        return self.author.username
