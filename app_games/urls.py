from django.urls import path
from app_games.views import games, tetris, snake, pong, bubbleshooter, pacman, spaceinvaders, slope, asteroid, dinosaur, snake2, dinosaur2, tetris2, asteroid2, pacman2, pong2

urlpatterns = [
    
    path('', games, name="games"),
    path('tetris/', tetris, name="tetris"),
    path('tetris2/', tetris2, name="tetris2"),
    path('bubbleshooter/', bubbleshooter, name="bubbleshooter"),
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
    
]