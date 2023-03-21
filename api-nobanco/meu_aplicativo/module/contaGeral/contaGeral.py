from django.db import models
from meu_aplicativo.models import Usuario

class ContaGeral(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.FloatField()
    tipo_conta = models.BooleanField()

    def __str__(self):
        return self.id
    