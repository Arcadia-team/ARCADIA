from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

#imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

#Actualizar info profile:
@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'app_perfiles/editar.html', {'form': form})
    

    
#imports
from app_perfiles.forms import UserUpdateForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#Actualizar info user:
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url =  reverse_lazy('inicio')
    template_name = 'app_perfiles/user_pannel.html'

    def get_object(self, queryset=None):
        return self.request.user


