from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone



from django.views.decorators.csrf import csrf_protect



from .models import Post, Comment, Reply, Users
from notification.models import Notification


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


########### View Post

def view_post(request, post):
    try:
        user = Users.objects.get(username=request.user)
    except:
        user = None
    post = get_object_or_404(Post, pk=post)

    context = {
        'post': post,
        'user' : user,
        'now': timezone.now,
    }
    template = 'post_detail.html'

    return render(request, template, context)







#### Remove Post
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
        author = Users.objects.get(username=request.user)
        post = Post.objects.get(pk=post)
        x = Comment.objects.create(
            author = author,
            post = post,
            content = content,
        )
        if author != post.author:
            Notification.objects.create(
                type='comment',
                sender=author,
                user=post.author,
                post=post,
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
            'comments': comments,

        }
        template = "comments/comments_area.html"
        return render(request, template, context)
    return redirect("timeline_page")


## like button for replies
def like_comment(request):
    if request.method == 'GET' and request.is_ajax():
        user = Users.objects.get(username=request.user)
        pk = request.GET.get('comment')
        comment = Comment.objects.get(id=pk)
        likes = comment.likes.all()
        if user not in likes:
            comment.likes.add(user)
            comment.save()
            if user != comment.author:
                Notification.objects.create(type='comment_like',
                                            sender=user,
                                            user=comment.author,
                                            post=comment.post,)
        else:
            comment.likes.remove(user)
            comment.save()
            try:
                note = Notification.objects.get(type='comment_like', sender=request.user, user=comment.author, post=comment.post)
                note.delete()
            except:
                pass

        return HttpResponse('success')
    return redirect("timeline_page")





### Remove comment
def remove_comment(request):
    if request.method == 'POST' and request.is_ajax():
        comment = request.POST.get('comment')
        if comment :
            comment = Comment.objects.get(id=comment)
            try:
                note = Notification.objects.get(type='comment', sender=comment.author.id, user=comment.post.author.id, post=comment.post.id)
                note.delete()
            except:
                pass

            comment.delete()



            return HttpResponse('success')

        return redirect("timeline_page")

    return redirect("timeline_page")





## Creat Replay fun
@csrf_protect
def creat_reply(request):
    if request.method == 'POST' and request.is_ajax():
        content = request.POST.get('content')
        comment = request.POST.get('comment')

        author = Users.objects.get(username=request.user)
        comment = Comment.objects.get(pk=comment)

        x = Reply.objects.create(
            author = author,
            comment = comment,
            content = content,
        )
        if author != comment.author:
            Notification.objects.create(
                type='reply',
                sender=author,
                user=comment.author,
                post=comment.post,
            )

        pk = x.pk
        reply = Reply.objects.get(pk=pk)
        context = {
            'reply': reply
        }
        template = "comments/created_reply.html"
        return render(request, template, context)
    return redirect('timeline_page')


### Remove Reply
def remove_reply(request):
    if request.method == 'POST' and request.is_ajax():
        reply = request.POST.get('reply')
        if reply :
            reply = Reply.objects.get(id=reply)
            try:
                note = Notification.objects.get(type='reply', sender=reply.author.id, user=reply.comment.author.id, post=reply.comment.post.id)
                note.delete()
            except:
                pass

            reply.delete()


            return HttpResponse('success')

        return redirect("timeline_page")

    return redirect("timeline_page")



## Get Replies that related to comment fun
def get_replies(request):
    if request.is_ajax():
        comment = request.GET.get('comment')
        user = Users.objects.get(username=request.user)
        replies = Reply.objects.filter(comment=comment).order_by('created_at')
        comment = Comment.objects.get(id=comment)

        context = {
            'user': user,
            'replies': replies,
            'comment': comment,
        }
        template = "comments/replies_area.html"
        return render(request, template, context)
    return redirect("timeline_page")


## like button for replies
def like_reply(request):
    if request.method == 'GET' and request.is_ajax():
        user = Users.objects.get(username=request.user)
        pk = request.GET.get('reply')
        reply = Reply.objects.get(id=pk)
        likes = reply.likes.all()
        if user not in likes:
            reply.likes.add(user)
            reply.save()
            if user != reply.author:
                Notification.objects.create(type='reply_like',
                                            sender=user,
                                            user=reply.author,
                                            post=reply.comment.post,)
        else:
            reply.likes.remove(user)
            reply.save()
            try:
                note = Notification.objects.get(type='reply_like', sender=request.user, user=reply.author, post=reply.comment.post)
                note.delete()
            except:
                pass

        return HttpResponse('success')
    return redirect("timeline_page")







## like button for posts
def like_button(request):
    if request.method == 'GET' and request.is_ajax():
        user = Users.objects.get(username=request.user)
        pk = request.GET.get('post')
        post = Post.objects.get(id=pk)
        likes = post.likes.all()
        if user not in likes:
            post.likes.add(user)
            post.save()
            if user != post.author:
                Notification.objects.create(type='like',
                                            sender=user,
                                            user=post.author,
                                            post=post,)
        else:
            post.likes.remove(user)
            post.save()
            try:
                note = Notification.objects.get(type='like', sender=request.user, user=post.author, post=post)
                note.delete()
            except:
                pass



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




def error_404_view(request, exception):
    return render(request, '404_page.html')