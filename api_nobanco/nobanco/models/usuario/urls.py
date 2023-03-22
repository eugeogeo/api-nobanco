""" http://seusite.com/usuarios/ - exibe o formulário para criar um novo usuário.
http://seusite.com/usuarios/1/ - exibe os detalhes do usuário com ID 1.
http://seusite.com/usuarios/1/atualizar/ - exibe o formulário para atualizar o usuário com ID 1.
http://seusite.com/usuarios/1/deletar/ - exibe a tela de confirmação para deletar o usuário com ID 1. """




from django.urls import path
from nobanco.models.usuario.views import (
    criar_usuario,
    atualiza_usuario,
    delete_usuario,
    detalhe_usuario,
    lista_usuario,
)

app_name = 'nobanco'

urlpatterns = [
    path('criar/', criar_usuario, name='criar_usuario'),
    path('atualizar/<int:pk>/', atualiza_usuario, name='atualiza_usuario'),
    path('deletar/<int:pk>/', delete_usuario, name='delete_usuario'),
    path('detalhe/<int:pk>/', detalhe_usuario, name='detalhe_usuario'),
    path('listar/', lista_usuario, name='lista_usuario'),
]
