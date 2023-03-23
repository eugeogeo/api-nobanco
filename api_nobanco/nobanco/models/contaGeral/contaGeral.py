from django.db import models
from nobanco.models.usuario.usuario import Usuario

class ContaGeral(models.Model):    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.FloatField()
    tipo_conta = models.BooleanField()

    