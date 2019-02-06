from django.shortcuts import render
from django import forms
from .models import Usuario
from login.forms_usuarios import UsuarioForm
from django.views.generic.base import TemplateView

class CadastrarUsuario(TemplateView):
    template_name = 'usuario.html'
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        form = UsuarioForm(request.POST)
        dados_form = form.data

            usuario = Usuario(nome=dados_form['nome'])
