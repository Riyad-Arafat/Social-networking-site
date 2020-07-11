from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login'),
    path('logout', views.log_out, name='logout'),
    path('<str:username>', views.profile, name='profile'),


]

