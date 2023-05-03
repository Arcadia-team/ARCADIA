from django.urls import path
from app_perfiles.views import edit_profile

urlpatterns = [
    path('', edit_profile, name="perfil"),
]