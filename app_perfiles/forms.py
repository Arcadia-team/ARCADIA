
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Avatar



class AvatarChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ruta_imagen


class EditProfileForm(forms.ModelForm):
    avatar = AvatarChoiceField(queryset=Avatar.objects.all(), label='Avatar', empty_label=None, to_field_name='ruta_imagen', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('avatar', 'bio', 'website',)
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

 

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