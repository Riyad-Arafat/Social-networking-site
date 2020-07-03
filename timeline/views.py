from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from posts.models import Post,Comment
from accounts.models import  Profile
from django.db.models import Q


# Create your views here.


################# TIME LINE VIEW #############################
def home_page(request):
    user = request.user
    if user.is_authenticated:
        user_authenticated = Profile.objects.get(user=request.user)
        posts = Post.objects.all().order_by('-created_at')
        comments = Comment.objects.all().order_by('-created_at')

        paginator = Paginator(posts,5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts: paginator.page(paginator.num_page)


        context = {
            'user' : user_authenticated,
            'posts' : posts,
            'comments' : comments,
        }
        template = "home.html"
        return render(request, template, context)

    return redirect('login')