from django.db import models

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cep = models. CharField(max_length=8)
    bloco = models.CharField(max_length=3)
    apartamento = models.CharField(max_length=4)
    complemento = models.CharField(max_length= 20)

class  Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    flag_delete = models.CharField(max_length=1)