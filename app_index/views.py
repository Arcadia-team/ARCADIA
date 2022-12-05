from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "app_index/index.html")

# Login
def login(request):
    return render(request, "app_index/login.html")

# Register
def signup(request):
    return render(request, "app_index/signup.html")