from django.urls import path
from app_perfiles.views import UserUpdateView

urlpatterns = [
    path('account/', UserUpdateView.as_view(), name="account"),

]