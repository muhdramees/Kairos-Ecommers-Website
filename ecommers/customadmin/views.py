from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

def custom_login(request):

    if 'email' in request.session:
        return redirect('customdashboard')

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            request.session['email'] = email
            return redirect("customdashboard")

        else:
            print("Invalid credential")

        return render (request, "login.html")

    return render(request, "customadmin/login.html")


def custom_dashboard(request):

    if 'email' in request.session:
        return render(request, "customadmin/dashboard.html")

    user_view = User.objects.all()
     
    return render(request, "customadmin/dashboard.html", {"user_view" : user_view})

def custom_logout(request):

    if 'email' in request.session:
        request.session.flush()

    return redirect('customlogin')