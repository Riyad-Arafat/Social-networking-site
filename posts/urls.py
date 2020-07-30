from django.urls import path
from . import views


urlpatterns = [
    path('create/post/', views.CreatePost, name="crate_post"),
    path('view/post/<int:post>', views.view_post, name="view_post"),
    path('remove/post/', views.RemovePost, name="remove_post"),
    path('get/comments/', views.get_comments, name='get_comments'),
    path('create/comment/', views.CreateComment, name='creat_comment'),
    path('comment/like/', views.like_comment, name='like_comment'),
    path('remove/comment/', views.remove_comment, name="remove_comment"),
    path('get/replies/', views.get_replies, name='get_replies'),
    path('create/reply/', views.creat_reply, name='create_reply'),
    path('remove/reply/', views.remove_reply, name='remove_reply'),
    path('reply/like/', views.like_reply, name='like_reply'),
    path('posts/count_views/', views.count_post_views, name='count_views'),
    path('post/like/', views.like_button, name='like_btn'),


]
