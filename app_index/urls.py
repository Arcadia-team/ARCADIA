from django.urls import path
from app_index.views import inicio, login


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),

    
]