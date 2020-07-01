from django.shortcuts import render, redirect
from posts.models import Post
from accounts.models import  Profile
from posts.forms import NewPost


# Create your views here.




################# TIME LINE VIEW #############################
def home_page(request):
    user = request.user
    if user.is_authenticated:
        user = Profile.objects.get(user=request.user)
        posts = Post.objects.all().order_by('-created_at')
        post_form = NewPost()
        new_post = None
        context = {
            'user' : user,
            'posts' : posts,
            'post_form' : post_form,
        }
        template = "home.html"

        if request.method == 'POST':
            post = NewPost(request.POST)
            if post.is_valid:
                new_post = post.save(commit=False)
                new_post.author = Profile.objects.get(username=request.user)
                new_post.save()
                post_form = NewPost()
        else:
            post_form = NewPost()

        return render(request, template, context)

    return redirect('login')