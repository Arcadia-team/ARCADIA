from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

#imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm


    

    
#imports
from app_perfiles.forms import UserUpdateForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#Actualizar info user:
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'app_perfiles/user_pannel.html'
    success_url =  reverse_lazy('account')

    def get_object(self, queryset=None):
        return self.request.user


