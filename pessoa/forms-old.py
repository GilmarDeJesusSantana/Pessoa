from django import forms
from .models import Pessoa

class PostForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome','titulo','cpf','telefone','cep','rua','numero','bairro','apartamento','bloco','complemento',)