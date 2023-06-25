from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)


class Maquina(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    processador = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    observacao = models.CharField(max_length=250)
