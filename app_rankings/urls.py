from django.urls import path
from app_rankings.views import rankings, ranking

urlpatterns = [
    path('', rankings, name="rankings"),
    path('ranking/', ranking, name="ranking"),
]