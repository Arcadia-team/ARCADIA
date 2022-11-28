from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def juegos(request):
    return render(request, "juegos.html")

def rankings(request):
    return render (request, "rankings.html")