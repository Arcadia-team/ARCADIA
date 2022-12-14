from django.urls import path
from app_index.views import inicio, login_request, signup_request


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login_request, name="login"),
    path('signup/', signup_request, name="signup"),
]