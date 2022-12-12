from django.shortcuts import render, redirect, reverse

#Login y register:
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from app_index.forms import UserSignupForm


# Create your views here.
def inicio(request):
    return render(request, "app_index/index.html")



# Login
def login(request):
    return render(request, "app_index/login.html")

# Register
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            mensaje = "Usuario creado, ¡Bienvenido a Arcadia!" 
            return render(request,"app_index/login.html",{"mensaje":mensaje})
            
    else: 
        form = UserSignupForm()
        return render(request, "app_index/signup.html",{"form":form})
    