from django.shortcuts import render

def login_view(request):
    return render(request, 'auth/login.html')

def dashboard_view(request):
    return render(request, 'auth/dashboard.html')