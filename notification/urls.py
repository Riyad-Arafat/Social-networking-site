from django.urls import path
from . import views


urlpatterns = [
    path('get/notifications', views.get_notifications, name="get_notifications"),
    path('read/notifications', views.read_notifications, name="read_notifications"),

]

