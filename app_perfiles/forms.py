
from django import forms
from django.contrib.auth.models import User
from app_perfiles.models import UserProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    avatar = forms.IntegerField()  # Agrega campos adicionales si es necesario

    
    def __init__(self, user_instance=None, user_profile_instance=None, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        if user_instance:
            self.fields['username'].initial = user_instance.username
            self.fields['email'].initial = user_instance.email
            self.fields['password'].initial = user_instance.password

        if user_profile_instance:
            self.fields['avatar'].initial = user_profile_instance.avatar