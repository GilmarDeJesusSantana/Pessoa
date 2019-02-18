from django.shortcuts import render
from django.views.generic.base import TemplateView
from pessoa.views import index
from login.forms_usuarios import UsuarioForm
class Login(TemplateView):
    template_login = 'login.html'

    def get(self,request):
        return render(request,self.template_login)

    def post(self,request):
        form = UsuarioForm(request.POST)
        if form.login_is_valid():
            return index(request)