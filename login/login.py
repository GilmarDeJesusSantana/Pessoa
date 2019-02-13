from django.shortcuts import render
from django.views.generic.base import TemplateView
from pessoa.views import index

class Login(TemplateView):
    template_login = 'login.html'

    def get(self,request):
        return render(request,self.template_login)

    def post(self,request):
        return index(request)