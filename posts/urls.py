from django.urls import path
from . import views

urlpatterns = [
    path('create/post', views.CreatePost, name="crate_post"),
    path('create/comment', views.CreateComment, name='creat_comment'),
    path('posts/count_views', views.count_post_views),
    path('get/comments', views.get_comments, name='get_comment'),

]
