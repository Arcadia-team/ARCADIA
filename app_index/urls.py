from django.urls import path
from app_index.views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio', inicio, name="inicio"),
    path('juegos', juegos, name="juegos"),
    path('rankings', rankings, name="rankings"),
    path('ranking', ranking, name="ranking"),
]