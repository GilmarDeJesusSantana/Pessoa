from django import forms
from django.contrib.auth.models import User
from login.models import Usuario
from django.db.models import Q


class UsuarioForm(forms.Form):
    print('-------Inicio da Classe-------')
    nome_user = forms.CharField(required=True)
    usuario = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    perfil = forms.CharField(required=False)

    def is_valid(self):
        valid = True
        if not super(UsuarioForm, self).is_valid():
            self.adiciona_erro('Verifique os dados informados.')
            valid = False
        user_exists = Usuario.objects.filter(nome_user__contains=self.data['nome_user'])
        if user_exists:
            self.adiciona_erro('Usuário já cadastrado.')
            valid = False
        return valid

    def login_is_valid(self):
        valid = True
        user = self.data['nome_user']
        senha = self.data['senha']
        # print('Usuario_Form .........', user)
        # print('Senha_Form...........', senha)
        user_login = Usuario.objects.get(usuario=user)
        print('Usuario_DataBase .........', user_login.usuario)
        print('Senha_DataBase............', user_login.senha)
        if  user_login.senha != senha:
            self.adiciona_erro('Usuário ou senha inválido')
            valid = False
            if user_login.nome_user != user:
                print('Segundo portao ||||||||')
                valid = False
        return valid

        # print('Usuario =======>>', user_login.senha, 'Para ser logado')
        # print ('Usuario ======> ', user_login_exists)

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
