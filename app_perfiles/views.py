from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

#formulario para actualizar
from app_perfiles.forms import UserUpdateForm

from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#Actualizar info user:
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url =  reverse_lazy('inicio')
    template_name = 'app_perfiles/user_pannel.html'

    def get_object(self, queryset=None):
        return self.request.user



