from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.

import re

class User(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    cellPhone = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        validatePassword(self.password)

def validatePassword(value):
    if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', value):
        raise ValidationError('A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um dígito.')

class GeneralAccount(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  value = models.FloatField()
  accountType = models.BooleanField()

class Balance(models.Model):
  accountId = models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
  value = models.FloatField()
  accountType = models.BooleanField()
  date = models.DateTimeField()   

class Purchase(models.Model):
  balanceId = models.ForeignKey(Balance, on_delete=models.CASCADE)
  value = models.FloatField()
  date = models.DateTimeField()
  place = models.CharField(max_length=100)