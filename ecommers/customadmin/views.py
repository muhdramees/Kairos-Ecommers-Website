from django.shortcuts import render, redirect

# Create your views here.

def customlogin(request):


    return render(request, "customadmin/login.html")


def customdashboard(request):
    return render(request, "customadmin/dashboard.html")