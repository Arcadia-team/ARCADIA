from django.urls import path
from app_games.views import games, tetris, snake, pong, flappybird, pacman, spaceinvaders, slope, asteroid, dinosaur, snake2, dinosaur2, tetris2, asteroid2, pacman2, pong2, flappybird2, bomberman

urlpatterns = [
    
    path('', games, name="games"),
    path('tetris/', tetris, name="tetris"),
    path('tetris2/', tetris2, name="tetris2"),
    path('flappybird/', flappybird, name="flappybird"),
    path('flappybird2/', flappybird2, name="flappybird2"),
    path('snake/', snake, name="snake"),
    path('snake2/', snake2, name="snake2"),
    path('pong/', pong, name="pong"),
    path('pong2/', pong2, name="pong2"),
    path('pacman/', pacman, name="pacman"),
    path('pacman2/', pacman2, name="pacman2"),
    path('spaceinvaders/', spaceinvaders, name="spaceinvaders"),
    path('slope/', slope, name="slope"),
    path('asteroid/', asteroid, name="asteroid"),
    path('asteroid2/', asteroid2, name="asteroid2"),
    path('dinosaur/', dinosaur, name="dinosaur"),
    path('dinosaur2/', dinosaur2, name="dinosaur2"),
    path('bomberman/', bomberman, name="bomberman"),
    
]