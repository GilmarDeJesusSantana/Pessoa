from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome_user = models.CharField(max_length = 100)
    usuario = models.CharField(max_length = 50)
    senha = models.CharField(max_length = 50)
    perfil = models.CharField(max_length = 10)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.nome_user