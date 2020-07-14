
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Community
from posts.models import Post
# Create your views here.



def community_page(request, pk):

    community   = get_object_or_404(Community, pk=pk)
    posts       = community.posts.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'community' : community,
        'posts' : posts

    }
    template = 'community.html'

    return render(request, template, context)