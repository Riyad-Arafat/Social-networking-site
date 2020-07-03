from django.urls import path
from . import views

urlpatterns = [
    path('create/post', views.CreatePost, name="crate_post"),
    path('create/comment',views.CreateComment, name='creat_comment'),

]
