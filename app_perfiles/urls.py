from django.urls import path
from app_perfiles.views import edit_profile, UserUpdateView

urlpatterns = [
    path('', edit_profile, name="profile"),
    path('account/', UserUpdateView.as_view(), name="account"),

]