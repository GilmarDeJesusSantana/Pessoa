from django.shortcuts import render
from .models import Usuario
from login.forms_usuarios import UsuarioForm
from django.views.generic.base import TemplateView

class CadastrarUsuario(TemplateView):
    template_name = 'usuario.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self,request, *args, **kwargs):
        form = UsuarioForm(request.POST)
        print('Antes da Validao do formulario.')
        if form.is_valid():
            dados_form = form.data
            usuario_login = Usuario(nome_user = dados_form['nome_user'],
                                    usuario   = dados_form['usuario'],
                                    senha     = dados_form['senha'],
                                    perfil    = dados_form['perfil']
                                  )
            usuario_login.save()
            return render(request,self.template_name)
        return render(request,self.template_name, {'form':form})