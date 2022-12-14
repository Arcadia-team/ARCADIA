from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#Register
class SignUpForm(UserCreationForm):    
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

#LOGIN
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"autofocus": False, 'class': 'inputs form-control input-block js-login-field'})
        self.fields['password'].widget.attrs.update({'class': 'inputs form-control form-control input-block js-password-field'}) 