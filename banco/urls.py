"""banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from usuarios.api.viewsets import UsuarioViewSet
from usuarios.api.viewsets import ContaGeralViewSet
from usuarios.api.viewsets import SaldoViewSet
from usuarios.api.viewsets import CompraViewSet
from usuarios.views import UsuarioCreateView, UsuarioList, UsuarioDetailView, UsuarioUpdateView
route = routers.DefaultRouter()

route.register(r'usuarios', UsuarioViewSet, basename='Usuarios')
route.register(r'contas', ContaGeralViewSet, basename='Contas')
route.register(r'saldos', SaldoViewSet, basename='Saldos')
route.register(r'compras', CompraViewSet, basename='Compras')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('listUser/', UsuarioList.as_view(), name='usuario_list'),
    path('deleteUser/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('updateUser/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('', include(route.urls)),
]

