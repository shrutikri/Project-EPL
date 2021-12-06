from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserDetails
from django.contrib.auth import authenticate

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('login.html')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email already exists!')
                return redirect('login.html')
            else:
                user = User.objects.create_user(username=username, first_name = first_name, last_name = last_name, email=email, password=password1,)
                user.save()
                messages.success(request, "Account successfully created!!")
                return redirect('login.html')   
        else:
            messages.info(request,'Password not Matching!')
            return redirect('register.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Try again!")
            return redirect('register.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def billing(request):
    return render(request, "billing.html")

def monitor(request):
    return render(request, "monitor.html")

def appliances(request):
    return render(request, "appliances.html")

def units(request):
    return render(request, "units.html")

def history(request):
    return render(request, "invoices.html")

def invoices(request):
    return render(request, "invoice-view.html")

def settings(request):
    return render(request, "profile-settings.html")

def change(request):
    return render(request, "change-password.html")

def about(request):
    return render(request, "about-us.html")

def forgot(request):
    return render(request, "forgot-password.html")

def privacy(request):
    return render(request, "privacy-policy.html")

def term(request):
    return render(request, "term-condition.html")
