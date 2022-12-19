from django.shortcuts import render, redirect, reverse

#Login y register:
from django.contrib.auth.forms import AuthenticationForm
from app_index.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from app_index.forms import SignUpForm


# Create your views here.
def inicio(request):
    return render(request, "app_index/index.html")

# Register
def signup_request(request):
    mensaje=""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request,"app_index/index.html",{"mensaje":"Usuario creado, ¡Bienvenido a Arcadia!"})
        
        mensaje="Please check your signup credentials and try again!"  
     
    form = SignUpForm()
    return render(request, "app_index/signup.html",{"form":form, "mensaje":mensaje})
    

# Login
def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data = request.POST)
        
        if form.is_valid(): #Comprueba que los campos "sintaxi" sea correcto, tipo de dato, etc.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user: #Comprueba que exista el usuario en la database
                login(request, user)
                return render(request, "app_index/index.html")
            else: 
                return render(request, "app_index/index.html",{"mensaje":"Error, datos incorrectos"})
        
        else: 
            return render(request, "app_index/index.html",{"mensaje":"Error, datos incorrectos"})
                
    else:   
        form = LoginForm()
        return render(request, "app_index/login.html",{"form":form})


# Logout
def logout_request(request):
    pass






#GAMES
def games(request):
    return render(request, "app_index/games.html")

#RANKINGS - General
def rankings(request):
    return render(request, "app_index/rankings.html")

#RANKING - POR JUEGO
def ranking(request):
    return render(request, "app_index/ranking.html")
