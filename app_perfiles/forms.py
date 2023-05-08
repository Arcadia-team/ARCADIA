
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
        fields = ['username', 'email']

    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Este email ya está en uso')
        return email

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if old_password and not authenticate(username=self.instance.username, password=old_password):
            raise forms.ValidationError('La contraseña actual es incorrecta.')

        if new_password1 and new_password1 != new_password2:
            raise forms.ValidationError('Las nuevas contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        new_password = self.cleaned_data.get('new_password1')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user
    