from django.shortcuts import render, redirect

# Create your views here.


def home_page(request):
    user = request.user
    if user.is_authenticated:
        context = {}
        template = "home.html"
        return render(request, template, context)
    return redirect('login')