from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    usuario = forms.CharField(required=True)
    senha   = forms.CharField(required=True)
    perfil  = forms.CharField(required= True)

    def is_valid(self):
        valid =True

        if not super(UsuarioForm,self).is_valid():
            self.adiciona_erro('Verifique os dados informados.')
            valid = False

        user_exists = User.objects.filter(nome=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro ('Usuário já cadastrado.')
            valid =False

    def adiciona_erro(self,message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)