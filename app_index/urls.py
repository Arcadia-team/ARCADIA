from django.urls import path
from app_index.views import inicio, login_request, signup_request, rankings, ranking, games, tetris, bubbleshooter, snake, pong


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login_request, name="login"),
    path('signup/', signup_request, name="signup"),
    path('games/', games, name="games"),
    path('rankings/', rankings, name="rankings"),
    path('ranking/', ranking, name="ranking"),
    path('tetris/', tetris, name="tetris"),
    path('bubbleshooter/', bubbleshooter, name="bubbleshooter"),
    path('snake/', snake, name="snake"),
    path('pong/', pong, name="pong"),
]