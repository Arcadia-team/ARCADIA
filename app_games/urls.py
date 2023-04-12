from django.urls import path
from app_games.views import games, tetris, snake, pong, bubbleshooter, pacman, spaceinvaders, slope, asteroid, dinosaur

urlpatterns = [
    
    path('', games, name="games"),
    path('tetris/', tetris, name="tetris"),
    path('bubbleshooter/', bubbleshooter, name="bubbleshooter"),
    path('snake/', snake, name="snake"),
    path('pong/', pong, name="pong"),
    path('pacman/', pacman, name="pacman"),
    path('spaceinvaders/', spaceinvaders, name="spaceinvaders"),
    path('slope/', slope, name="slope"),
    path('asteroid/', asteroid, name="asteroid"),
    path('dinosaur/', dinosaur, name="dinosaur"),
    
]