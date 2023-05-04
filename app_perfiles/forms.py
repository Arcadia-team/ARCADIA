
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Avatar



class AvatarChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ruta_imagen


class EditProfileForm(forms.ModelForm):
    avatar = AvatarChoiceField(queryset=Avatar.objects.all(), label='Avatar', empty_label=None, to_field_name='ruta_imagen', widget=forms.Select(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=30, label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('avatar', 'bio', 'website',)
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        instance = super().save(commit=False)
        user = instance.user
        user.username = self.cleaned_data['username']
        if commit:
            instance.save()
            user.save()
        return instance
 