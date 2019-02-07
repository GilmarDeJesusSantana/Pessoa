from django.shortcuts import render
from .models import Usuario
from login.forms_usuarios import UsuarioForm
from django.views.generic.base import TemplateView

class CadastrarUsuario(TemplateView):
    template_name = 'usuario.html'
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print('Validacao----')
        else:
            print('Validao is fa')
        dados_form = form.data
        usuario_login = Usuario(nome      = dados_form['nome'],
                                usuario   = dados_form['usuario'],
                                senha     = dados_form['senha'],
                                perfil    = dados_form['perfil']
                              )
        usuario_login.save()
        return render(request,self.template_name)