from django.urls import path
from . import views

urlpatterns = [
    path('create/post/', views.CreatePost, name="crate_post"),
    path('create/comment/', views.CreateComment, name='creat_comment'),
    path('posts/count_views/', views.count_post_views, name='count_views'),
    path('post/like/', views.like_button, name='like_btn'),
    path('get/comments/', views.get_comments, name='get_comments'),

]
