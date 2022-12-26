from django.shortcuts import render

# Create your views here.

#RANKINGS - General
def rankings(request):
    return render(request, "app_rankings/rankings.html")

#RANKING - POR JUEGO
def ranking(request):
    return render(request, "app_rankings/ranking.html")