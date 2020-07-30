from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth import authenticate, logout, login

from .forms import UserRegistrationForm, UserLoginForm, UserForm, ProfileForm
from django.contrib import messages

from .models import Profile, Users
from posts.models import Comment
from notification.models import Notification


from django.conf import settings
import os


from django.http import HttpResponse



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
            messages.success(request, 'You have successfully registered. Login now')
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
            user = Users.objects.get(email=email)
            user.is_online = True
            user.save()
            if user.first_login:
                user.first_login = False
                user.save()
                return redirect("edit_profile", user.username)


            return redirect("timeline_page")
        else:
            messages.warning(request, 'The username and password you entered did not match our records. Please check '
                                      'inputs and try again.')
    else:
        form = UserLoginForm()

    context = {

        'form': form
    }


    template = 'registration/login.html'
    return render(request, template, context)


################################ logout ###################################33

def log_out(request):
    user = Users.objects.get(username=request.user)
    user.is_online = False
    user.save()
    logout(request)
    return redirect('/')







##################### PROFILE VIEW ############################

def profile(request, username):
    x = request.user
    if x.is_authenticated:
        user = Users.objects.get(username=x)
    else:
        user = None

    profile_user = get_object_or_404(Profile, user__username=username)
    posts = profile_user.user.posts.all().order_by('-created_at')
    comments = Comment.objects.all().order_by("-created_at")
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    ### View all media files related to user
    media_root = settings.MEDIA_ROOT
    try:
        pictures   = os.listdir(f'{media_root}/profile/{profile_user.id}/picture')[:3]
        pictures   = reversed(pictures)

    except:
        pictures = None

    try:
        covers      = os.listdir(f'{media_root}/profile/{profile_user.id}/cover')[:3]
        covers      = reversed(covers)
    except:
        covers = None

    try:
        images      = os.listdir(f'{media_root}/profile/{profile_user.id}/posts')[:3]
        images      = reversed(images)
    except:
        images = None



    context = {

        'user': user,
        'profile' : profile_user,
        'pictures' : pictures,
        'covers' : covers,
        'images' : images,
        'media_url' : f"{settings.MEDIA_URL}\profile\{profile_user.id}",
        'posts' : posts,
        'comments': comments,
        'now': timezone.now
    }
    template = 'profile.html'

    return render(request, template, context)



################# Edit profile #############333
def edit_profile(request, username):

    if request.user.is_authenticated:
        user = get_object_or_404(Users, username=username)
        if request.user == user:
            if request.method == 'POST':
                user_form = UserForm(request.POST, instance=user)
                profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
                if user_form.is_valid and profile_form.is_valid :
                    user_form.save()
                    profile_form.save()
                    messages.success(request, 'Your profile has been updated')
                    username = user_form.cleaned_data['username']
                    return redirect('edit_profile', username)
            else:
                user_form = UserForm(instance=user)
                profile_form = ProfileForm(instance=user.profile)

            context = {
                'user_form' : user_form,
                'profile_form' : profile_form
            }
            template = 'edit_profile.html'
            return render(request, template, context)
        else:
            return redirect('timeline_page')
    else:
        return redirect('timeline_page')



############ follow profile #######################

def follow(request):
    if request.user.is_authenticated and request.is_ajax():
        pk = request.GET['id']
        user = Users.objects.get(username=request.user)
        user2 = Users.objects.get(profile=pk)
        profile1 = Profile.objects.get(id=pk)

        following = user.profile.following.all()
        if user2 not in following:
            user.profile.following.add(user2)
            user.profile.save()
            profile1.followers.add(request.user)
            profile1.save()
            Notification.objects.create(type='follow',
                                        sender=user,
                                        user=user2,)
        else:
            user.profile.following.remove(user2)
            user.profile.save()
            profile1.followers.remove(request.user)
            profile1.save()
            try:
                note = Notification.objects.get(type='follow', sender=user, user=user2)
                note.delete()
            except:
                pass




        return HttpResponse('')
