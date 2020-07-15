from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth import authenticate, logout, login

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

from .models import Profile, Users
from posts.models import Comment , Post




from django.http import HttpResponse, HttpResponseRedirect
from urlextract import URLExtract


# Create your views here.


################################# SIGNUP FORM VIEW #########################

def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect("timeline_page")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {

        'form': form
    }

    template = 'registration/sign_up.html'
    return render(request, template, context)




######################### LOGIN FORM VIEW #############################3


def login_form(request):
    user = request.user
    if user.is_authenticated:
        return redirect("timeline_page")
    if request.method == 'POST':
        form = UserLoginForm()
        email       = request.POST['email']
        password    = request.POST['password']
        user        = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("timeline_page")
        else:
            messages.warning(request, 'The username and password you entered did not match our records. Please double-check and try again.')
    else:
        form = UserLoginForm()

    context = {

        'form': form
    }


    template = 'registration/login.html'
    return render(request, template,context)


################################ logout ###################################33

def log_out(request):
    logout(request)
    return redirect('/')








##################### PROFILE VIEW ############################

def profile(request, username):
    x = request.user
    if x.is_authenticated:
        user = Profile.objects.get(username=x)
    else:
        user = None

    profile_user = get_object_or_404(Profile, username=username)
    posts = profile_user.posts.all().order_by('-created_at')
    comments = Comment.objects.all().order_by("-created_at")
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    context = {

        'user': user,
        'profile' : profile_user,
        'posts' : posts,
        'comments': comments,
        'now': timezone.now
    }
    template = 'profile.html'

    return render(request, template, context)


############ follow profile #######################

def follow(request):
    if request.user.is_authenticated and request.is_ajax():
        pk = request.GET['id']
        user = Profile.objects.get(username=request.user)
        user2 = Users.objects.get(profile=pk)
        profile1 = Profile.objects.get(id=pk)

        following = user.following.all()
        if user2 not in following:
            user.following.add(user2)
            user.save()
            profile1.followers.add(request.user)
            profile1.save()
        else:
            user.following.remove(user2)
            user.save()
            profile1.followers.remove(request.user)
            profile1.save()




        return HttpResponse('')
