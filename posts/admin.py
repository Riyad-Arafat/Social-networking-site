from django.contrib import admin
from .models import Post
from accounts.models import Profile
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.author:
            author = Profile.objects.get(user=request.user)
            obj.author = author
            obj.save()
        obj.save()

admin.site.register(Post,PostAdmin)