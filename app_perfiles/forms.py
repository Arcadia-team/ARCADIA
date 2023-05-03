
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