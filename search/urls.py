from django.urls import path
from . import views


urlpatterns = [
    path('search/result/', views.search, name='search'),
    path('search/result/q=<str:query>/posts/', views.more_posts, name='more_posts'),


]

