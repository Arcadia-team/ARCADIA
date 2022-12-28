from django.urls import path
from app_games.views import games, tetris, snake, pong, bubbleshooter

urlpatterns = [
    
    path('', games, name="games"),
    path('tetris/', tetris, name="tetris"),
    path('bubbleshooter/', bubbleshooter, name="bubbleshooter"),
    path('snake/', snake, name="snake"),
    path('pong/', pong, name="pong"),
]