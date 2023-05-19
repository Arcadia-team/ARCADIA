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

#Para crear perfil default: 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#Buscador
from app_games.models import Game
from app_games.models import Score
from django.http import HttpResponse
import json

#Para conseguir los juegos mas jugados
from django.db.models import F

#Grafica adminpanel 
import matplotlib.pyplot as plt
from django.http import JsonResponse
from io import BytesIO
import base64
import matplotlib
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
import re


def userpanel(request):
    if request.method == 'POST':
        imageID = request.POST.get('imageID')
        user = request.user.username
        if imageID == 'pacman':
            idimagen = 1
        elif imageID == 'ghostazulfuerte':
            idimagen = 2
        elif imageID == 'ghostazul':
            idimagen = 3
        elif imageID == 'ghostrosa':
            idimagen = 4
        elif imageID == 'ghostnaranja':
            idimagen = 5
        elif imageID == 'ghostverde':
            idimagen = 6
        elif imageID == 'ghostrojo':
            idimagen = 7
        elif imageID == 'ghostblanco':
            idimagen = 8
        usuario = UserProfile.objects.filter(user_id__username=user).values('avatar_id').update(avatar_id=idimagen)
        return HttpResponse("Import añadido")
            



def adminpanel(request):
    if request.user.username == 'juanfran':
        #if request.method == 'POST':
        queryset = Game.objects.values('name','numPartidas')
        valores = [dato['numPartidas'] for dato in queryset]
        etiquetas = [dato['name'] for dato in queryset]

        # Crear un gráfico de queso con Plotly
        fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
        fig.add_trace(go.Pie(labels=etiquetas, values=valores), 1, 1)
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20)
        fig.update_layout(
            plot_bgcolor='rgb(12,22,45)',
            paper_bgcolor='rgb(12,22,45)'
        )

        fig.update_layout(
            showlegend=True,
            legend=dict(
                title='Etiquetas',
                font=dict(
                    color='yellow'
                )
            )
        )
        fig.update_layout(
            height=600,
            width=600,
            margin=dict(l=50, r=50, t=50, b=50)
            # otras propiedades...
        )


        # Devolver el gráfico de Plotly como una respuesta de Django
        div = fig.to_html(full_html=False)



        partidas = Score.objects.filter(game_id=1).order_by('-score')


        return render(request,"app_index/adminpanel.html",{"div" : div,'partidas' : partidas})
    else:
        return HttpResponse("Lo siento, no tienes acceso a esta página.")




def adminpanel2(request):
        if request.method == 'POST':
            valores2 = request.POST.get('val2')
            valores3 = request.POST.get('val3')
            valores4 = request.POST.get('val4')
            if valores2 != None:
                Score.objects.filter(user_profile_id__user__username=valores2, score=valores3).delete()


            valorSeleccionado = request.POST.get('selectjuegos')
            partidas = Score.objects.filter(game_id=valorSeleccionado).values('user_profile__user__username','score','date_played').order_by('-score')
            resultados_dict = list(partidas)
            return JsonResponse(resultados_dict, safe=False)
                #return render(request,"app_index/adminpanel.html",{'partidas':partidas})
        else:
            return HttpResponse("Lo siento, no tienes acceso a esta página.")

def adminpanel3(request):
    if request.method == 'POST':
        val = request.POST.get('val1')
        val2 = request.POST.get('val2')
        clickid = request.POST.get('id')
        print(clickid)
        juego = request.POST.get('juego')
        patron1 = r"^[a-zA-Z0-9_]+$"
        if re.match(patron1, val):
            if len(clickid) == 6:
                ultimo_caracter = clickid[-1]
                ultimo_caracter_int = int(ultimo_caracter)
                ultimo_caracter_int = ultimo_caracter_int - 1
                ultimo_caracter2 = clickid[:-1]
            elif len(clickid) == 7:
                ultimo_caracter = clickid[-2]
                ultimo_caracter_int = int(ultimo_caracter)
                ultimo_caracter_int = ultimo_caracter_int - 1
                ultimo_caracter2 = clickid[:-2]
            else:
                ultimo_caracter = clickid[-1]
                ultimo_caracter_int = int(ultimo_caracter)
                ultimo_caracter_int = ultimo_caracter_int - 1
                ultimo_caracter2 = clickid[:-1]

            if ultimo_caracter2 == 'score':
                print('val '+ val)
                print('val2 '+ val2)
                print(juego)
                

                userExist = Score.objects.filter(score=val2).values('id').order_by('-score')
                print(userExist)
                userid = userExist[0]['id']

                print(ultimo_caracter_int)
                valores5 = Score.objects.filter(game_id=juego).values('user_profile_id','score','date_played').order_by('-score')[ultimo_caracter_int]
                print(valores5)

                mi_objeto = Score(user_profile_id=valores5['user_profile_id'],score=val,date_played=valores5['date_played'],game_id=juego)
                print(mi_objeto)
                mi_objeto.save()

                Score.objects.filter(user_profile_id=valores5['user_profile_id'],score=val2,date_played=valores5['date_played'],game_id=juego).delete()

                return HttpResponse("La cadena solo puede contener numeros, letras y los siguientes simbolos _ score", content_type='application/json')

            elif ultimo_caracter2 == 'user':
                print('val '+ val)
                print('val2 '+ val2)
                print('juego '+str(juego))

                variableParaIF = UserProfile.objects.filter(user__username=val).values('user_id')

                print('VarableParaIF '+str(variableParaIF))

                if len(variableParaIF) > 0:
                    userExist = UserProfile.objects.filter(user__username=val2).values('user_id')[:1]
                    print('userExist '+str(userExist))
                    userid = userExist[0]['user_id']

                    print('userid '+str(userid))
                    print('Ultimo Caracter'+str(ultimo_caracter_int))

                    valores5 = Score.objects.filter(game_id=juego).values('user_profile_id','score','date_played').order_by('-score')[ultimo_caracter_int]
                    print('valores5' +str(valores5))




                    mi_objeto = Score(user_profile_id=variableParaIF[0]['user_id'],score=valores5['score'],date_played=valores5['date_played'],game_id=juego)
                    print(mi_objeto)
                    mi_objeto.save()

                    Score.objects.filter(user_profile_id__user__username=val2,score=valores5['score'],date_played=valores5['date_played'],game_id=juego).delete()

                    return HttpResponse("La cadena solo puede contener numeros, letras y los siguientes simbolos _", content_type='application/json')
            else:
                print('4')
        else:
            print("La cadena solo puede contener numeros, letras y los siguientes simbolos _ else")
            error_message = "La cadena solo puede contener numeros, letras y los siguientes simbolos _"
            response_data = {'error': error_message,'val':val2}
            return HttpResponse(json.dumps(response_data), content_type='application/json')

        return HttpResponse("La cadena solo puede contener numeros, letras y los siguientes simbolos _", content_type='application/json')





# Create your views here.
def inicio(request):
    partidas = Game.objects.order_by('-numPartidas').values_list('name', flat=True)[:3]
    partida1 = partidas[0].lower()
    fototop1 = 'foto'+partida1
    
    partida2 = partidas[1].lower()
    fototop2 = 'foto'+partida2

    partida3 = partidas[2].lower()
    fototop3 = 'foto'+partida3

    print(partida1)
    print(partida2)
    print(partida3)

    return render(request, "app_index/index.html",{'top1':partida1,'top2':partida2,'top3':partida3,'fototop1':fototop1,'fototop2':fototop2,'fototop3':fototop3})


def game_to_dict(game):
    if game.count() == 1:
        return {
            '0': game[0].name
        }
    if game.count() == 2:
        return {
            '0': game[0].name,
            '1': game[1].name
        }
    if game.count() == 3:
        return {
            '0': game[0].name,
            '1': game[1].name,
            '2': game[2].name
        }

def inicio2(request):
    if request.method == 'POST':
        letra = request.POST['letra']
        games = Game.objects.filter(name__icontains=letra)[:3]
        games_list = [game_to_dict(games) for game in games]
        return HttpResponse(json.dumps(games_list), content_type='application/json')


# Register
def signup_request(request):
    mensaje=""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #guardamos info user y procedemos a crear perfil con foto.
            form.save()
            
            #Redirige a inicio dando la bienvenida
            return render(request,"app_index/index.html",{"mensaje":"User created, ¡Welcome to Arcadia!"})
        
        mensaje="Please check your signup credentials and try again!"  
     
    form = SignUpForm()
    return render(request, "app_index/signup.html",{"form":form, "mensaje":mensaje})

#Crear user_profile default: 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



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


    


