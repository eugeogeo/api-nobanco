from rest_framework import viewsets
from users.api import serializers
from rest_framework.permissions import IsAuthenticated
from users import models

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = serializers.UserSerializer
  queryset = models.User.objects.all()

class GeneralAccountViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.GeneralAccountSerializer
  queryset = models.GeneralAccount.objects.all()

class BalanceViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.BalanceSerializer
  queryset = models.Balance.objects.all()

class PurchaseViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.PurchaseSerializer
  queryset = models.Purchase.objects.all()
