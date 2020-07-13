from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from django.views.decorators.csrf import csrf_protect





from .models import Post, Comment, Profile, Users

# Create your views here.


## create post fun
@csrf_protect
def CreatePost(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST['content']
        Post.objects.create(
            author = Profile.objects.get(username=request.user),
            content = content)

        return HttpResponseRedirect(reverse("timeline_page"))
    return redirect("timeline_page")




## Creat comment fun
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









## Get comments that related to post fun
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


## like button
def like_button(request):
    if request.method == 'GET' and request.is_ajax():
        user = Users.objects.get(username=request.user)
        pk = request.GET['post']
        post = Post.objects.get(id=pk)
        likes = post.likes.all()
        if user not in likes:
            post.likes.add(user)
            post.save()
        else:
            post.likes.remove(user)
            post.save()

        context = {
            'user': user,
            'post': post
        }
        template = "post-box.html"
        return render(request, template, context)

    return redirect("timeline_page")






## Count views of posts that show in time line
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



