from django.shortcuts import render
from app_games.models import Score

# Create your views here.

#RANKINGS - General
def rankings(request):
    snake = Score.objects.filter(game_id='1').order_by('-score')[:3]
    pacman = Score.objects.filter(game_id='2').order_by('-score')[:3]
    tetris = Score.objects.filter(game_id='3').order_by('-score')[:3]
    dinosaur = Score.objects.filter(game_id='4').order_by('-score')[:3]
    asteroid = Score.objects.filter(game_id='5').order_by('-score')[:3]
    slope = Score.objects.filter(game_id='6').order_by('-score')[:3]
    pong = Score.objects.filter(game_id='7').order_by('-score')[:3]
    bomberman = Score.objects.filter(game_id='8').order_by('-score')[:3]
    

    return render(request, "app_rankings/rankings.html", {'snake':snake, 'tetris':tetris, 'pacman':pacman, 'dinosaur':dinosaur, 'asteroid':asteroid, 'slope':slope, 'pong':pong, 'bomberman':bomberman })

#RANKING - POR JUEGO
def ranking(request):
    if request.method == 'POST':
        boton_id = request.POST.get('boton_id')
        boton_id_foto = 'foto'+ boton_id.lower()
        if boton_id == 'PONG':
            pong = Score.objects.filter(game_id='7').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'SLOPE':
            pong = Score.objects.filter(game_id='6').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'SNAKE':
            pong = Score.objects.filter(game_id='1').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'TETRIS':
            pong = Score.objects.filter(game_id='3').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'ASTEROID':
            pong = Score.objects.filter(game_id='5').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'PACMAN':
            pong = Score.objects.filter(game_id='2').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'DINOSAUR':
            pong = Score.objects.filter(game_id='4').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})
        if boton_id == 'BOMBERMAN':
            pong = Score.objects.filter(game_id='8').order_by('-score')[:10]
            return render(request, 'app_rankings/ranking.html', {'boton_id': boton_id,'pong': pong,'boton_id_foto':boton_id_foto})

