from django.db.models import Count
from django.utils import timezone


from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache


from posts.models import Post
from accounts.models import Users, Profile
from django.db.models import Q



import urllib3

# Create your views here.


################# TIME LINE VIEW #############################
def home_page(request):
    cache.clear()
    user = request.user
    if user.is_authenticated:
        user = Users.objects.get(username=request.user)
        ##
        if user.profile.following.count() < 4 :
            accounts = Profile.objects.all().annotate(followers_count=Count('followers')).order_by('-followers_count')
        else:
            accounts = None


        ## Paginator Posts
        posts = Post.objects.filter(Q(author=request.user) | Q(author__in=user.profile.following.all())).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)



        ############# check if user is online ################

        context = {
            'user' : user,
            'posts' : posts,
            'accounts' : accounts,
            'now': timezone.now,


        }
        template = "home.html"
        return render(request, template, context)

    return redirect('login')

