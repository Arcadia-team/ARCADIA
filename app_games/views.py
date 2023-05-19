from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse
from app_games.models import Score
from app_games.models import Game
from django.db.models import F
import time
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json


# Las vistas con el nombre del juego cargar el juego en la web.
# Las vistas con el nombre del juego y un 2 al final cargan las scores en la db

def verificar_usuario_registrado(username):
    try:
        User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False


#GAMES
def games(request):
    return render(request, "app_games/games.html")

#GAME - JUEGOS
def tetris(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=3)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/tetris.html")
    else:
        return redirect(reverse('login'))

def tetris2(request):
    score = request.POST.get('score') 
    score = int(score)
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=3).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=3,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')

def flappybird(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=9)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/flappybird.html")
    else:
        return redirect(reverse('login'))

def flappybird2(request):
    score = request.POST.get('score') 
    score = int(score)
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=9).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=9,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')

def bomberman(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=8)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/bomberman.html")
    else:
        return redirect(reverse('login'))

@csrf_exempt
def bomberman2(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    score = body_data.get('score')
    print(score)
    score = int(score)
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=8).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=8,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')
    


def snake(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=1)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/snake.html")
    else:
        return redirect(reverse('login'))

def snake2(request):
    score = request.POST.get('score')
    if score != '0':
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=1).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=1,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')
        

def pong(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=7)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/pong.html")
    else:
        return redirect(reverse('login'))

def pong2(request):
    score = request.POST.get('score') 
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=7).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=7,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')
def pacman(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=2)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/pacman.html")
    else:
        return redirect(reverse('login'))

def pacman2(request):
    score = request.POST.get('score') 
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=2).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=2,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')

def slope(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=6)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/slope.html")
    else:
        return redirect(reverse('login'))

def asteroid(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=5)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/asteroid.html")
    else:
        return redirect(reverse('login'))

def asteroid2(request):
    score = request.POST.get('score')  
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=5).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=5,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')

def dinosaur(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        numPartidas = Game.objects.get(id=4)
        numPartidas.numPartidas = F('numPartidas') + 1
        numPartidas.save()
        return render(request, "app_games/dinosaur.html")
    else:
        return redirect(reverse('login'))

def dinosaur2(request):
    score = request.POST.get('score') 
    if score != 0:
        user_id = request.user.id
        comprobarScore = Score.objects.filter(score=score,user_profile_id=user_id,game_id=4).values('id')
        if len(comprobarScore) == 0:
            VariableScore = Score(score=score,game_id=4,user_profile_id=user_id)
            VariableScore.save()
            return HttpResponse('query enviada')
        else:
            return HttpResponse('query no enviada, score repetido')
    return HttpResponse('query no enviada, score es 0')