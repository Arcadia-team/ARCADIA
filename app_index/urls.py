from django.urls import path
from app_index.views import inicio


urlpatterns = [
    path('', inicio, name="inicio"),
    
]