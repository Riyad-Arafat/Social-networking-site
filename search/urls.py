from django.urls import path
from . import views


urlpatterns = [
    path('search/result/', views.search, name='search'),
    path('top/hashtag/', views.hash_tag, name='hash_tag'),
    path('search/result/q=<str:query>/posts/', views.more_posts, name='more_posts'),


]

