from django.urls import path
from . import views


urlpatterns = [
    path('search/result/', views.search, name='search'),
    path('top/hash_tag/<str:tag>/result/', views.get_hash_tag, name='get_hash_tag'),
    path('search/result/q=<str:query>/posts/', views.more_posts, name='more_posts'),


]

