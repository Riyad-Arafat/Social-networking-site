from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from accounts.models import  Profile
from django.db.models import Q


# Create your views here.


################# TIME LINE VIEW #############################
def home_page(request):
    user = request.user
    if user.is_authenticated:
        user_authenticated = Profile.objects.get(user=request.user)


        try:
            posts = Post.objects.filter(~Q(viewers=user)).order_by('-created_at')
        except:

            posts = None


        context = {
            'user' : user_authenticated,
            'posts' : posts,
        }
        template = "home.html"
        return render(request, template, context)

    return redirect('login')