from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#Register
class SignUpForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['email'].widget.attrs.update({'class':'signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['password1'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['password2'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
            
#LOGIN
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'inputs form-control input-block js-login-field'})
        self.fields['password'].widget.attrs.update({'class': 'inputs form-control form-control input-block js-password-field'}) 