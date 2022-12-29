from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from kairos.models import EmailUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import adduser
from kairos.models import EmailUser
# Create your views here.

def custom_login(request):

    if 'email' in request.session:
        return redirect('custom_dashboard')

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            request.session['email'] = email
            return redirect("custom_dashboard")

        else:
            print("Invalid credential")

        return render (request, "login.html")

    return render(request, "customadmin/login.html")


def custom_dashboard(request):

    if 'email' in request.session:
        return render(request, "customadmin/dashboard.html")
     
    return render(request, "customadmin/dashboard.html", {"user_view" : user_view})

def custom_logout(request):

    if 'email' in request.session:
        request.session.flush()

    return redirect('custom_login')



def user_view(request):
    User = EmailUser
    user = User.objects.all()

    return render(request, "customadmin/userview.html", {'users' : user})


def custom_adduser(request):

    User = EmailUser
    

    form = adduser(request.POST)

    if request.method == 'POST':
        form = adduser(request.POST)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 == password2:
            
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email is Already Taken")
                return render(request, 'customadmin/userview.html', {'forms' : form})

            else:
                user = User.objects.create_superuser(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,"User Created")
                return redirect('custom_login')

        else:
            messages.info(request, "Password not match")
            return render(request, "customadmin/adduser.html", {'form' : form })


    return render(request, "customadmin/adduser.html", {'form' : form})  
