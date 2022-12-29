from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "index.html")
    

def user_login(request):

    if 'email' in request.session:
        return redirect('home')
        

    if request.method == 'POST':
        form = LoginForm(request.POST)
   

        if form.is_valid():

            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            


            if user is not None:
                request.session['email'] = email
                # login(request,user)
                return redirect('home')

            else:
                 messages.add_message(request, messages.ERROR, "Invalid Credentials", extra_tags='alert-danger')                           
                            
            return render(request, 'login.html', {'form': form})
    
    form = LoginForm()  
    return render(request, "login.html", {'form': form})
   

    

    
# @login_required(login_url="/login")
def home(request):

    if 'email' in request.session:
        return render(request, "homepage.html")

    return redirect('user_login')

    

# @login_required(login_url="/")
def user_logout(request):
    
    if 'email' in request.session:
        request.session.flush()

    return redirect('user_login')


def user_signup(request):


    return render(request, 'signup.html')
    
    
    
  
    