from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_protect


from rest_framework.response import Response


from .models import Post, Comment, Profile, Users
# Create your views here.



@csrf_protect
def CreatePost(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST['content']
        Post.objects.create(
            author = Profile.objects.get(username=request.user),
            content = content)

        return HttpResponseRedirect(reverse("timeline_page"))
    return redirect("timeline_page")


@csrf_protect
def CreateComment(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST['content']
        post = request.POST['post']

        x = Comment.objects.create(
            author = Users.objects.get(username=request.user),
            post = Post.objects.get(id=post),
            content = content,
        )
        pk = x.pk
        comment = Comment.objects.get(pk=pk)
        context = {
            'comment': comment
        }
        template = "comments/created_comment.html"
        return render(request, template, context)
    return redirect('timeline_page')










def get_comments(request):
    if request.method == 'GET' and request.is_ajax():
        post = request.GET['post']
        user = Profile.objects.get(user=request.user)
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        context = {
            'user': user,
            'comments': comments
        }
        template = "comments/comments_area.html"
        return render(request, template, context)
    return redirect("timeline_page")


def count_post_views(request):
    if request.user.is_authenticated and request.is_ajax():
        user = Users.objects.get(username=request.user)
        pk = request.GET['id']
        post = Post.objects.get(id=pk)
        viewers = post.viewers.all()
        if user not in viewers:
            post.viewers.add(user)
            post.save()

        return HttpResponse('')
    return redirect("timeline_page")
