from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "index.html")

# Login
def login(request):
    return render(request, "login.html")

# Register
def signup(request):
    return render(request, "signup.html")