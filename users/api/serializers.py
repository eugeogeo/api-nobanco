from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','cpf', 'email', 'cellPhone', 'name', 'password')

class GeneralAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeneralAccount
        fields = ('users', 'value', 'accountType')

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Balance
        fields = ('accountId', 'value', 'accountType', 'date')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = ('balanceId', 'value', 'date', 'place')