from rest_framework import serializers
from usuarios import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ('cpf', 'email', 'celular', 'nome', 'senha')

class ContaGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContaGeral
        fields = ('usuario', 'valor', 'tipo_conta')

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saldo
        fields = ('id_conta', 'valor', 'tipo_conta', 'data')

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compra
        fields = ('id_saldo', 'valor', 'data', 'local')