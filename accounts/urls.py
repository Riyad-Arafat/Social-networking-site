from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login'),
    path('profil/<str:username>/edit', views.edit_profile, name='edit_profile'),
    path('logout', views.log_out, name='logout'),
    path('<str:username>', views.profile, name='profile'),
    path('follow/profile', views.follow, name='follow'),
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')




]

