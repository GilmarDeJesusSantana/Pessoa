from django import forms
from django.contrib.auth.models import User
from login.models import Usuario

class UsuarioForm(forms.Form):
    nome_user = forms.CharField(required=True)
    usuario = forms.CharField(required=True)
    senha   = forms.CharField(required=True)
    perfil  = forms.CharField(required= True)

    def is_valid(self):
        valid =True
        if not super(UsuarioForm,self).is_valid():
            self.adiciona_erro('Verifique os dados informados.')
            valid = False
        user_exists = Usuario.objects.filter(nome_user__contains=self.data['nome_user'])
        if user_exists:
            self.adiciona_erro ('Usuário já cadastrado.')
            valid = False
        return valid

    def login_is_valid(self):
        valid = True
        usuario= self.data['nome_user']
        senha= self.data['senha']
        user_login = Usuario.objects.get(nome_user=usuario)

        if user_login.nome_user == usuario && user_login.senha == senha:
            return render


        print('Usuario =======>>', user_login.senha, 'Para ser logado')
        print ('Usuario ======> ', user_login_exists)

    def adiciona_erro(self,message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)