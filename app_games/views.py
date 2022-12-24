from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


# Create your views here.

#GAMES
def games(request):
    return render(request, "app_games/games.html")