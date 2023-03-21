from django.db import models

class Usuario(models.Model):

    id = models. IntegerField(primary_key=True)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=80)

    def __str__(self):
        return self.id
    