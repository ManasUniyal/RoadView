from django.shortcuts import render


# Create your views here.

def welcomeUser(request):
    if request.user.is_authenticated:
        return render(request, 'main/home.html')
    else:
        return render(request, 'welcome/welcome.html')
