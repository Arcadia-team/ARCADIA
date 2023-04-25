from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


#Login y register:
from django.contrib.auth.forms import AuthenticationForm
from app_index.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from app_index.forms import SignUpForm
from app_perfiles.models import UserProfile

#Para crear perfil default: 
from django.db.models.signals import post_save
from django.dispatch import receiver
from app_perfiles.models import UserProfile
from django.contrib.auth.models import User

#Buscador
from app_games.models import Game
from django.http import HttpResponse
import json

#Para conseguir los juegos mas jugados
from django.db.models import F

# Create your views here.
def inicio(request):
    partidas = Game.objects.order_by('-numPartidas').values_list('name', flat=True)[:3]
    partida1 = partidas[0].lower()
    fototop1 = 'foto'+partida1
    
    partida2 = partidas[1].lower()
    fototop2 = 'foto'+partida2

    partida3 = partidas[2].lower()
    fototop3 = 'foto'+partida3

    return render(request, "app_index/index.html",{'top1':partidas[0],'top2':partidas[1],'top3':partidas[2],'fototop1':fototop1,'fototop2':fototop2,'fototop3':fototop3})


def game_to_dict(game):
    if game.count() == 1:
        return {
            '0': game[0].name
        }
    if game.count() == 2:
        return {
            '0': game[0].name,
            '1': game[1].name
        }
    if game.count() == 3:
        return {
            '0': game[0].name,
            '1': game[1].name,
            '2': game[2].name
        }

def inicio2(request):
    if request.method == 'POST':
        letra = request.POST['letra']
        games = Game.objects.filter(name__icontains=letra)[:3]
        games_list = [game_to_dict(games) for game in games]
        return HttpResponse(json.dumps(games_list), content_type='application/json')


# Register
def signup_request(request):
    mensaje=""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #guardamos info user y procedemos a crear perfil con foto.
            form.save()
            
            #Redirige a inicio dando la bienvenida
            return render(request,"app_index/index.html",{"mensaje":"User created, ¡Welcome to Arcadia!"})
        
        mensaje="Please check your signup credentials and try again!"  
     
    form = SignUpForm()
    return render(request, "app_index/signup.html",{"form":form, "mensaje":mensaje})

#Crear user_profile default: 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



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
                return redirect(reverse('inicio'))
            
        form = LoginForm()
        return render(request, "app_index/login.html",{"form":form, "mensaje":"Incorrect data"})
    
    #Sino es POST:         
    form = LoginForm()
    return render(request, "app_index/login.html",{"form":form})
    


# Logout
def logout_request(request):
    logout(request)
    return redirect(reverse('inicio'))


    


