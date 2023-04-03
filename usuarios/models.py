from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.

import re

class Usuario(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        validate_senha(self.senha)

def validate_senha(value):
    if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', value):
        raise ValidationError('A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um dígito.')

class ContaGeral(models.Model):    
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  valor = models.FloatField()
  tipo_conta = models.BooleanField()

class Saldo(models.Model):
  id_conta = models.ForeignKey(ContaGeral, on_delete=models.CASCADE)
  valor = models.FloatField()
  tipo_conta = models.BooleanField()
  data= models.DateTimeField()   

class Compra(models.Model):
  id_saldo = models.ForeignKey(Saldo, on_delete=models.CASCADE)
  valor = models.FloatField()
  data = models.DateTimeField()
  local = models.CharField(max_length=100)