from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #noticias
    path('list/', views.list_news, name='list_news'),
    path('add/', views.add_news, name='add_news'),
    path('edit/<int:pk>/', views.edit_news, name='edit_news'),
    path('delete/<int:pk>/', views.delete_news, name='delete_news'),

    #periodistas
    path('journalists/', views.journalist_list, name='journalist_list'),
    path('journalists/add/', views.add_journalist, name='add_journalist'),
    path('journalists/edit/<int:pk>/', views.edit_journalist, name='edit_journalist'),
    path('journalists/delete/<int:pk>/', views.delete_journalist, name='delete_journalist'),

    #Categorias
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('categoria/', views.categoria, name='categoria'),
    path('politica/', views.politica, name='politica'),
    path('entretenimiento/', views.entretenimiento, name='entretenimiento'),
    path('internacional/', views.internacional, name='internacional'),
    path('deporte/', views.deporte, name='deporte'),
    #FIN CATEGORIA

    #INICIO CONTACTO
    path('contacto/', views.contacto, name='contacto'),
    #FIN CONTACTO
    
    path('planes/', views.planes, name='planes'),

    #INICIO DE SESSION
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #FIN DE SESSION
]
