from django.shortcuts import render


# Create your views here.

def loginPage(request):
    return render(request, 'authentication/login.html')

def registerPage(request):
    return render(request, 'authentication/register.html')
