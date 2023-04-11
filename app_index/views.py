from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


#Login y register:
from django.contrib.auth.forms import AuthenticationForm
from app_index.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from app_index.forms import SignUpForm
from app_perfiles.models import UserProfile

# Create your views here.
def inicio(request):
    return render(request, "app_index/index.html")

# Register
def signup_request(request):
    mensaje=""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #guardamos info user y procedemos a crear perfil con foto.
            form.save()

            # Crear automáticamente un UserProfile con una foto por defecto.
            default_photo_path = 'profile_photos/default_profile_photo.png' 
            user_profile = UserProfile(user=user, photo=default_photo_path)

            #Redirige a inicio dando la bienvenida
            return render(request,"app_index/index.html",{"mensaje":"User created, ¡Welcome to Arcadia!"})
        
        mensaje="Please check your signup credentials and try again!"  
     
    form = SignUpForm()
    return render(request, "app_index/signup.html",{"form":form, "mensaje":mensaje})
    

# Login
def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data = request.POST)
        
        if form.is_valid(): #Comprueba que los campos "sintaxi" sea correcto, tipo de dato, etc.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user: #Comprueba que exista el usuario en la database
                login(request, user)
                return redirect(reverse('inicio'))
            
        form = LoginForm()
        return render(request, "app_index/login.html",{"form":form, "mensaje":"Incorrect data"})
    
    #Sino es POST:         
    form = LoginForm()
    return render(request, "app_index/login.html",{"form":form})
    


# Logout
def logout_request(request):
    logout(request)
    return redirect(reverse('inicio'))
    


