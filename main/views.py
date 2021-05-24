from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'main/homepage.html')
        else:
            return render(request, 'welcome/welcome.html')


def result(request):
    if request.method == 'POST':
        return render(request, 'main/result.html')
