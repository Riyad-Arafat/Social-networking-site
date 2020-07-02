from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Post,Profile
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