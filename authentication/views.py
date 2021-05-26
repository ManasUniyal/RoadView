from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        email_address = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email_address, password=password)
        if user:
            login(request, user)
            return redirect('main:home')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('authentication:login')

    return render(request, 'authentication/login.html')


def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email_address = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=email_address).exists():
            User.objects.create_user(username=email_address,
                                     first_name=first_name,
                                     last_name=last_name,
                                     password=password)
            messages.success(request, 'Account created successfully')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Email already registered')
            return redirect('authentication:register')

    return render(request, 'authentication/register.html')


def logoutUser(request):
    logout(request)
    return redirect('welcome:welcome')
