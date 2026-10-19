from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def login_view(request):
    # Temporary fallback or login template logic
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('dogs:home')