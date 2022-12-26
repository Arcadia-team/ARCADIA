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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            mensaje = "Usuario creado, ¡Bienvenido a Arcadia!" 
        else:
            mensaje="Ha ocurrido un error, comprueba que has introducido correctamente los campos."
        
        return render(request,"app_index/index.html",{"mensaje":mensaje})
            
    else: 
        form = SignUpForm()
        return render(request, "app_index/signup.html",{"form":form})
    

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


#GAMES - GENERAL
def games(request):
    return render(request, "app_index/games.html")

#GAME - POR JUEGO
def tetris(request):
    return render(request, "app_index/tetris.html")

def bubbleshooter(request):
    return render(request, "app_index/bubbleshooter.html")

def snake(request):
    return render(request, "app_index/snake.html")

def pong(request):
    return render(request, "app_index/pong.html")

#RANKINGS - GENERAL
def rankings(request):
    return render(request, "app_index/rankings.html")

#RANKING - POR JUEGO
def ranking(request):
    return render(request, "app_index/ranking.html")
