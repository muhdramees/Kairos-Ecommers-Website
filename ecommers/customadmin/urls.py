
from django.urls import path
from . import views

urlpatterns = [
       path('', views.customlogin , name="customlogin"),
       path('dashboard/', views.customdashboard , name="customdashboard"),
]