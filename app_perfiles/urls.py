from django.urls import path
from app_perfiles.views import UserUpdateView

urlpatterns = [
    path('', UserUpdateView.as_view(), name="update_user"),
]