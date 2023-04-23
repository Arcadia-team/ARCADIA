from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse
from app_games.models import Score


# Las vistas con el nombre del juego cargar el juego en la web.
# Las vistas con el nombre del juego y un 2 al final cargan las scores en la db

#GAMES
def games(request):
    return render(request, "app_games/games.html")

#GAME - JUEGOS
def tetris(request):
    return render(request, "app_games/tetris.html")

def tetris2(request):
    
    score = request.POST.get('score') 
    user_id = request.user.id
    VariableScore = Score(score=score,game_id=3,user_profile_id=user_id)
    VariableScore.save()
    return HttpResponse('query enviada')

def bubbleshooter(request):
    return render(request, "app_games/bubbleshooter.html")

def snake(request):
    return render(request, "app_games/snake.html")

def snake2(request):
    score = request.POST.get('score')
    if score != '0':
        print('asdasd')
        user_id = request.user.id
        #user_ip = request.META.get('REMOTE_ADDR')
        #print(user_ip)
        VariableScore = Score(score=score,game_id=1,user_profile_id=user_id)
        VariableScore.save()
    return HttpResponse('query enviada')
        

def pong(request):
    return render(request, "app_games/pong.html")

def pong2(request):
    score = request.POST.get('score') 
    user_id = request.user.id
    VariableScore = Score(score=score,game_id=7,user_profile_id=user_id)
    VariableScore.save()
    return HttpResponse('query enviada')

def pacman(request):
    return render(request, "app_games/pacman.html")

def pacman2(request):
    score = request.POST.get('score') 
    user_id = request.user.id
    VariableScore = Score(score=score,game_id=2,user_profile_id=user_id)
    VariableScore.save()
    return HttpResponse('query enviada')

def spaceinvaders(request):
    return render(request, "app_games/spaceinvaders.html")

def slope(request):
    return render(request, "app_games/slope.html")

def asteroid(request):
    return render(request, "app_games/asteroid.html")

def asteroid2(request):
    score = request.POST.get('score')  
    user_id = request.user.id
    VariableScore = Score(score=score,game_id=5,user_profile_id=user_id)
    VariableScore.save()
    return HttpResponse('query enviada')

def dinosaur(request):
    return render(request, "app_games/dinosaur.html")

def dinosaur2(request):
    
    score = request.POST.get('score') 
    user_id = request.user.id
    VariableScore = Score(score=score,game_id=4,user_profile_id=user_id)
    VariableScore.save()

    return HttpResponse('query enviada')