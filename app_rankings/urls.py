from django.urls import path
from app_rankings.views import rankings, ranking, rankings_personal

urlpatterns = [
    path('', rankings, name="rankings"),
    path('rank/', rankings_personal, name="rank"),
    path('ranking/', ranking, name="ranking"),
]