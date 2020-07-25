from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import Notification

from accounts.models import Users
# Create your views here.



def get_notifications(request):
    if request.method == 'GET' and request.is_ajax():
        user = Users.objects.get(username=request.user)
        notifications = Notification.objects.filter(Q(user=user) | Q(all=user)).order_by('-created_at')

        context = {
            'notifications' : notifications
        }
        template = 'notifications.html'

        return render(request, template, context)
    return redirect('timeline_page')




def read_notifications(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = Users.objects.get(username=request.user)
            notifications = Notification.objects.filter(user=user, readable=False)
            for i in notifications:
                i.readable = True
                i.save()
            return HttpResponse('')


        return redirect('timeline_page')
    return redirect('timeline_page')