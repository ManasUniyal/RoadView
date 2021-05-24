from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'main/homepage.html')


def result(request):
    if request.method == 'POST':
        return render(request, 'main/result.html')
