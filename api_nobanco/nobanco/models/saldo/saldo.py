from django.db import models
from nobanco.models.contaGeral.contaGeral import ContaGeral

class Saldo(models.Model):
    id = models.IntegerField(primary_key=True)
    id_conta = models.ForeignKey(ContaGeral, on_delete=models.CASCADE)
    valor = models.FloatField()
    tipo_conta = models.BooleanField()
    data= models.DateTimeField()

    def __str__(self):
        return self.id
    