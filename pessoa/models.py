from django.db import models

# Create your models here.

class  Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    titulo= models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    flag_delete = models.CharField(max_length=1)
    #Endereco
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    bloco = models.CharField(max_length=3)
    apartamento = models.CharField(max_length=4)
    complemento = models.CharField(max_length=20)
    def publish(self):
        self.save()

    def __str__(self):
        return self.nome
