from django.urls import path
from . import views

urlpatterns = [
    path('create/post/', views.CreatePost, name="crate_post"),
    path('vies/post/<int:post>', views.view_post, name="view_post"),
    path('remove/post/', views.RemovePost, name="remove_post"),
    path('create/comment/', views.CreateComment, name='creat_comment'),
    path('remove/comment/', views.remove_comment, name="remove_comment"),
    path('posts/count_views/', views.count_post_views, name='count_views'),
    path('post/like/', views.like_button, name='like_btn'),
    path('get/comments/', views.get_comments, name='get_comments'),

]
