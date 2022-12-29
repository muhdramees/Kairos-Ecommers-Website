
from django.urls import path
from . import views

urlpatterns = [
       path('', views.custom_login , name="custom_login"),
       path('dashboard/', views.custom_dashboard , name="custom_dashboard"),
       path('logout/', views.custom_logout , name="custom_logout"),
       path('userview/', views.user_view , name="user_view"),
       path('adduser/', views.custom_adduser , name="custom_adduser"),

]