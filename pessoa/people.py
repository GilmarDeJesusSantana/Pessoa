from django.shortcuts import render
from pessoa.search import SearchPeople
from pessoa.forms import RegistraPessoaForm
from .models import Pessoa
from django.db.models import Q
from django.views.generic.base import TemplateView

class PeopleDetails(TemplateView):
    template_details = 'details.html'
    def get(self,request, pessoa_id):
        print('Classe People Details, ID da Pessoa' +  pessoa_id)
        people = Pessoa.objects.filter(Q(id=pessoa_id))
        return render(request,self.template_details,{'pessoas':people})

class PeopleSearch(TemplateView):
    template_search = 'pessoa_search.html'
    def get(self,request):
        return render(request,self.template_search)

    def post(self,request):
        form_search = SearchPeople(request.POST)
        dados_search = form_search.data

        #Usei o metodo isdigit() da classe string para verificar se é um numero.
        if dados_search['nome'].isdigit():
            people_search = Pessoa.objects.filter(Q(titulo__startswith=dados_search['nome']))
        else:
            people_search = Pessoa.objects.filter(Q(nome__startswith=dados_search['nome']))

        return render(request, self.template_search, {'pessoas': people_search})

class CadastroPessoaView(TemplateView):
    template_name = 'pessoaForm.html'
    # este metodo envia o html para o browser
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        """A Classe chamada abaixo Valida o formulario"""
        form = RegistraPessoaForm(request.POST)
        dados_form = form.data

        pessoa = Pessoa(nome=dados_form['nome'],
                        titulo= dados_form['titulo'],
                        cpf=dados_form['cpf'],
                        telefone= dados_form['telefone'],
                        flag_delete='A',
                        email= dados_form['email'],
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