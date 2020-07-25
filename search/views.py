from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from posts.models import Post, Comment
from accounts.models import Users
from django.db.models import Q


# Create your views here.


#### search view

def search(request):
    user = request.user
    if user.is_authenticated:
        try:
            q = request.GET.get("q")
        except:
            q = None
        if q:
            posts = Post.objects.filter(Q(content__contains=q)).order_by('-created_at')[:5]
            accounts = Users.objects.filter(Q(first_name__contains=q.split(" ")[0]) | Q(last_name__contains=q.split(" ")[-1]) | Q(username__contains=q))
            context = {
                'query' : q,
                'posts' : posts,
                'accounts' : accounts,
            }
            template = 'search/search_page.html'
            return render(request , template, context)
        else:
            return redirect('timeline_page')
    else:
        return redirect('timeline_page')



def more_posts(request, query):
    posts = Post.objects.filter(Q(content__contains=query)).order_by('-created_at')
    page = request.GET.get('', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }

    template = 'search/more_posts.html'
    return render(request, template, context)



### Hash_tags #####

def get_hash_tag(request, tag):
    user = request.user
    if user.is_authenticated:
        user = Users.objects.get(username=request.user)

        tag = '#'+tag
        posts = Post.objects.filter(Q(content__iregex=tag)).order_by('-created_at')
        count = posts.count()
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
            'user' : user,
            'query': tag,
            'posts': posts,
            'count' : count,
            'now' : timezone,

        }
        template = 'search/hash_tag.html'
        return render(request, template, context)