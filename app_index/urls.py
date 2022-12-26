from django.urls import path
from app_index.views import inicio, login_request, signup_request, logout_request


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login_request, name="login"),
    path('logout/',  logout_request, name="logout"),
    path('signup/', signup_request, name="signup"),

]