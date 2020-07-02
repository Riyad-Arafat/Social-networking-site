from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login

from .forms import UserRegistrationForm, UserLoginForm
from .models import  Profile


# Create your views here.


################################# SIGNUP FORM VIEW #########################

def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home_page")
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


def loginForm(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home_page")

    if request.method == 'POST':
        form = UserLoginForm()
        email       = request.POST['email']
        password    = request.POST['password']
        user        = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("timeline_page")

    else:
        form = UserLoginForm()

    context = {

        'form': form
    }


    template = 'registration/login.html'
    return  render(request, template,context)





##################### PROFILE VIEW ############################

def profile(request,username):
    user = request.user
    profile = get_object_or_404(Profile ,username=username)
    posts = profile.posts.all().order_by('-created_at')
    context = {

        'user': user,
        'profile' : profile,
        'posts' : posts,
    }
    template = 'profile.html'



    return render(request, template, context)