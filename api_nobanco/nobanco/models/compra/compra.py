from django.db import models
from nobanco.models.saldo.saldo import Saldo

class Compra(models.Model):
    id = models.IntegerField(primary_key=True)
    id_saldo = models.ForeignKey(Saldo, on_delete=models.CASCADE)
    valor = models.FloatField()
    data = models.DateTimeField()
    local = models.CharField(max_length=100)

