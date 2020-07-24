from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone



from django.views.decorators.csrf import csrf_protect



from .models import Post, Comment, Users


# Create your views here.


## create post fun

@csrf_protect
def CreatePost(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST.get('content')
        image   = request.FILES.get('image')
        community = request.POST.get('community')
        if community != 'none':
            post = Post.objects.create(
                author=Users.objects.get(username=request.user),
                content=content,
                community_id=community
            )
        else:
            post = Post.objects.create(
                author=Users.objects.get(username=request.user),
                content=content,
                image=image,
            )
        pk = post.pk
        post = Post.objects.get(pk=pk)
        context = {
            'post': post,
            'now': timezone.now,
        }

        template = "post-box.html"
        return render(request, template, context)


    return redirect("timeline_page")

## Remove Post

def RemovePost(request):
    if request.method == 'POST' and request.is_ajax():
        post = request.POST.get('post')
        if post :
            post = Post.objects.get(id=post)
            image = post.image
            if image:
                image.delete()

            post.delete()


            return HttpResponse('success')

        return redirect("timeline_page")

    return redirect("timeline_page")



## Creat comment fun
@csrf_protect
def CreateComment(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST.get('content')
        post = request.POST.get('post')
        print(post)

        x = Comment.objects.create(
            author = Users.objects.get(username=request.user),
            post = Post.objects.get(pk=post),
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
    if request.is_ajax():
        post = request.GET.get('post')
        user = Users.objects.get(username=request.user)
        comments = Comment.objects.filter(post_id=post).order_by('-created_at')
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
        pk = request.GET.get('post')
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
        pk = request.GET.get('id')
        post = Post.objects.get(id=pk)
        viewers = post.viewers.all()
        if user not in viewers:
            post.viewers.add(user)
            post.save()

        return HttpResponse('')
    return redirect("timeline_page")



