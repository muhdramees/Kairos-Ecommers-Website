
from django.urls import path
from . import views

urlpatterns = [
       path('', views.custom_login , name="customlogin"),
       path('dashboard/', views.custom_dashboard , name="customdashboard"),
       path('logout/', views.custom_logout , name="customlogout"),

]