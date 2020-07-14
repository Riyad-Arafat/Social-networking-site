from django.urls import path
from . import views


urlpatterns = [

    path('community/id=<int:pk>', views.community_page),

]

