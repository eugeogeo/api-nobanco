from django.contrib import admin
from django.urls import path

from .views import criar_usuario, atualiza_usuario, delete_usuario, detalhe_usuario, lista_usuario

urlpatterns = [
    path('', criar_usuario, name='criar_usuario'),
    path('', atualiza_usuario, name='atualiza_usuario'),
    path('', delete_usuario, name='delete_usuario'),
    path('', detalhe_usuario, name='detalhe_usuario'),
    path('', lista_usuario, name='lista_usuario'),
] 
