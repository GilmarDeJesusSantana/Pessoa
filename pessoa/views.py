from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from .models import Pessoa
from pessoa.forms import RegistraPessoaForm
from django import forms

def index(request):
    pessoas = Pessoa.objects.all()
    return render(request,'index.html',{'pessoas':pessoas})


class CadastroPessoaView(TemplateView):
    template_name = 'pessoaForm.html'


    # este metodo envia o html para o browser
    def get(self, request):
        print('Metodo chamado----> GET.')
        return render(request, self.template_name)
        print('Render processado-->')

    def post(self, request):
        form = RegistraPessoaForm(request.POST)
        dados_form = form.data
        print('Metodo chamado----> Post')
        pessoa = Pessoa(nome=dados_form['nome'],
                        titulo= dados_form['titulo'],
                        cpf=dados_form['cpf'],
                        telefone= dados_form['telefone'],
                        flag_delete='A',
                        rua=dados_form['rua'],
                        numero=dados_form['numero'],
                        bairro=dados_form['bairro'],
                        cep=dados_form['cep'],
                        bloco=dados_form['bloco'],
                        apartamento=dados_form['apartamento'],
                        complemento=dados_form['complemento']
        )
        pessoa.save()
        print ('Dados Registrados!!')
        return render(request,'pessoaForm.html')
#def post(self, request):
#    pass