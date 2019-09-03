from django.db import models

# Create your models here.

class Pais(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Regiao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

