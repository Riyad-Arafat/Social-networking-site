from django.shortcuts import render, redirect
from accounts.models import Users, Profile

# Create your views here.


def home_page(request):
    user = request.user
    if user.is_authenticated:
        user = Users.objects.get(username=request.user)
        context = {
            'user' : user,
        }
        template = "home.html"
        return render(request, template, context)
    return redirect('login')