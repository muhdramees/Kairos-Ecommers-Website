
from django.urls import path
from . import views

urlpatterns = [
       path('', views.index , name="index"),
       path('login/', views.user_login , name="user_login"),
       path('home/', views.home , name="home"),
       path('logout/', views.user_logout, name="user_logout"),
       path('signup/', views.user_signup, name="user_signup"),
]