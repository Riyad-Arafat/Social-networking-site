from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Post, Comment ,Profile , Users
# Create your views here.



@csrf_protect
def CreatePost(request):

    if request.method == 'POST':
        content = request.POST['content']

        Post.objects.create(
            author= Profile.objects.get(username=request.user),
            content = content
        )
        return HttpResponse("")


@csrf_protect
def CreateComment(request):
    if request.method == 'POST':
        content = request.POST['content']
        post = request.POST['post']

        Comment.objects.create(
            author= Users.objects.get(username=request.user),
            post= Post.objects.get(id=post) ,
            content = content,
        )
        return HttpResponse("")
