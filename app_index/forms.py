from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#Register
class SignUpForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    #Comprobación de existencia de email:
    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return valid

        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')
            return False
        return True
    
    # Estilo de los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['email'].widget.attrs.update({'class':'signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['password1'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
        self.fields['password2'].widget.attrs.update({'class':'form-control js-continue-input js-continue-focus-target signup-input form-control input-block flex-1 border-0 rounded-0 p-0 box-shadow-none color-text-white f4 text-mono'})
            
#LOGIN
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        # Username input
        self.fields['username'].widget.attrs.update({
        'style':'background-color:#0D1117; color: #C9D1D9;',
        'class': 'form-control input-block js-login-field', 
        'id':'login_field',
        'name':'login',
        'autocorrect':'off'})

        # Password input
        self.fields['password'].widget.attrs.update({
            'class':'form-control input-block js-password-field',
            'style':'background-color:#0D1117; color: #C9D1D9;'}) 