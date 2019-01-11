from django import forms
from django.contrib.auth.models import User
from .peopleUtils import adiciona_erro
class RegistraPessoaForm(forms.Form):

    nome        = forms.CharField(required=True)
    titulo      = forms.CharField(required=True)
    cpf         = forms.CharField(required=False)
    telefone    = forms.CharField(required=False)
    cep         = forms.CharField(required=False)
    rua         = forms.CharField(required=False)
    numero      = forms.CharField(required=False)
    bairro      = forms.CharField(required=False)
    apartamento = forms.CharField(required=False)
    bloco       = forms.CharField(required=False)
    complemento = forms.CharField(required=False)

    def is_valid(self):
        valid = True
        if not super(RegistraPessoaForm, self).is_valid():
            adiciona_erro('Por favor, verifique os dados informados!!')
            valid = False
        user_exists = User.objects.filter(nome=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro ('Pessoa já cadastrada!')
            valid = False