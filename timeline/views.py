import random
from django.utils import timezone


from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache


from posts.models import Post, Comment
from accounts.models import Profile, Users
from django.db.models import Q


# Create your views here.


################# TIME LINE VIEW #############################
def home_page(request):
    cache.clear()
    user = request.user
    if user.is_authenticated:
        user = Users.objects.get(username=request.user)
        posts = Post.objects.filter(Q(author__followers=user) | Q(author=user.profile)).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
            'user' : user.profile,
            'posts' : posts,
            'now': timezone.now

        }
        template = "home.html"
        return render(request, template, context)

    return redirect('login')


