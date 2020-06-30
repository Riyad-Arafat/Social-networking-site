from django.shortcuts import render, redirect
from accounts.models import  Profile

# Create your views here.


def home_page(request):
    user = request.user
    if user.is_authenticated:
        user = Profile.objects.get(user=request.user)
        context = {
            'user' : user,
        }
        template = "home.html"
        return render(request, template, context)
    return redirect('login')