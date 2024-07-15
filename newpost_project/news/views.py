from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views.decorators.csrf import csrf_exempt
import requests

def index(request):
    news_list = News.objects.all()
    response = requests.get('https://mindicador.cl/api')
    indicators = response.json() if response.status_code == 200 else {}
    

    return render(request, 'news/index.html', {'news_list': news_list, 'indicators': indicators})

#INCIO CATEGORIAS
def categoria(requst):
    return render(requst, 'news/Categoria/categoria.html')

def tecnologia(request):
    return render(request, 'news/Categoria/subcategoria/tecnologia.html')

def politica(requst):
    return render(requst, 'news/Categoria/subcategoria/politica.html')

def entretenimiento(requst):
    return render(requst, 'news/Categoria/subcategoria/entretenimiento.html')

def internacional(requst):
    return render(requst, 'news/Categoria/subcategoria/internacional.html')

def deporte(requst):
    return render(requst, 'news/Categoria/subcategoria/deporte.html')

def internacional(requst):
    return render(requst, 'news/Categoria/subcategoria/internacional.html')
#FIN CATEGORIAS

#INICIO CONTACTO

def contacto(requst):
    return render(requst, 'news/contacto/contacto.html')

#FIN CONTACTO

#INICIO PLANES

def planes(requst):
    return render(requst, 'news/subcripciones/planes.html')

#FIN PLANES


#Inicio Crud Noticias
def list_news(request):
    newss = News.objects.all()
    return render(request, 'news/crud noticias/list_news.html', {News:newss})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_news')
    else:
        form = NewsForm()
    return render(request, 'news/crud noticias/list_news.html ', {'form': form})

def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('list_news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/crud noticias/edit_news.html', {'form': form})

def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('list_news')
#Fin crud Noticias

#Inicio Crud Periodistas
def journalist_list(request):
    journalists = Journalist.objects.all()
    return render(request, 'news/crud periodistas/journalist_list.html', {'journalists': journalists})

def add_journalist(request):
    if request.method == 'POST':
        form = JournalistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journalist_list')
    else:
        form = JournalistForm()
    return render(request, 'news/crud periodistas/add_journalist.html', {'form': form})

def edit_journalist(request, pk):
    journalist = get_object_or_404(Journalist, pk=pk)
    if request.method == 'POST':
        form = JournalistForm(request.POST, instance=journalist)
        if form.is_valid():
            form.save()
            return redirect('journalist_list')
    else:
        form = JournalistForm(instance=journalist)
    return render(request, 'news/crud periodistas/edit_journalist.html', {'form': form})

def delete_journalist(request, pk):
    journalist = get_object_or_404(Journalist, pk=pk)
    journalist.delete()
    return redirect('journalist_list')
#Fin crud Periodistas

#inicio de sesion
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('news/index.html')  # Reemplaza 'ruta_principal' por la URL a la que deseas redirigir después del login
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'news/login/login.html')

def user_logout(request):
    logout(request)
    return redirect('news/login/login.html')

#fin de inicio de sesion