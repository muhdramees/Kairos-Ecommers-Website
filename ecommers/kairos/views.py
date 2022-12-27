from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def user_login(request):


    


    return render(request, "login.html")

def home(request):
    return render(request, "homepage.html")