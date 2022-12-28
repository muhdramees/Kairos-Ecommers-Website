from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, "index.html")
    

def user_login(request):

    if 'email' in request.session:
        return redirect('home')
        print("**********************************")

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)


        if user is not None:
            request.session['email'] = email
            return redirect('home')

        else:
            print("Invalid Credential")
        
        return render(request, 'login.html')

    return render(request, "login.html")

    

def home(request):

    if 'email' in request.session:
        return render(request, "homepage.html")

    return redirect('user_login')


def user_logout(request):
    
    if 'email' in request.session:
        request.session.flush()

    return redirect(user_login)