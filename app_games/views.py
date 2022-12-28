from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


# Create your views here.

#GAMES
def games(request):
    return render(request, "app_games/games.html")


#GAME - JUEGOS
def tetris(request):
    return render(request, "app_games/tetris.html")

def bubbleshooter(request):
    return render(request, "app_games/bubbleshooter.html")

def snake(request):
    return render(request, "app_games/snake.html")

def pong(request):
    return render(request, "app_games/pong.html")