from django.urls import path
from app_games.views import games 

urlpatterns = [
    
    path('', games, name="games"),

]