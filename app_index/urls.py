from django.urls import path
from app_index.views import inicio, login, signup


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
]