from django.shortcuts import render, redirect
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.models import User
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
    User = get_user_model()
    form = SignupForm(request.POST)
    

    if request.method == 'POST':

        form = SignupForm(request.POST)

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email already taken...")
                
                return render(request, 'signup.html', {'form' : form})

            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "User Created")
                return redirect('user_login')

        else:
            messages.info(request, "Password not match")
            return render(request, 'signup.html', {'form' : form})

    
    return render(request, 'signup.html', {'form' : form})
    
    
    
  
    