from rest_framework import viewsets
from usuarios.api import serializers
from usuarios import models

class UsuarioViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UsuarioSerializer
  queryset = models.Usuario.objects.all()

class ContaGeralViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.ContaGeralSerializer
  queryset = models.ContaGeral.objects.all()

class SaldoViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.SaldoSerializer
  queryset = models.Saldo.objects.all()

class CompraViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CompraSerializer
  queryset = models.Compra.objects.all()
