from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def result(request):
    if request.method == 'POST':
        return render(request, 'main/result.html')
