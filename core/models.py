from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    ##Mostrar o nome na consulta
    def __str__(self):
        return self.nome
