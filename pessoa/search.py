from django import forms
from django.contrib.auth.models import User
from .peopleUtils import adiciona_erro


class SearchPeople(forms.Form):
    nome    = forms.CharField(required=True)
    titulo  = forms.CharField(required=False)
    def is_valid(self):
        valid = True
        if not super(SearchPeople, self).is_valid():
            adiciona_erro('Dados para pesquisa iválido, informe um nome ou numero de titulo.')
            valid = False

        people_exists = User.objects.filter(nome=self.data['nome']).exists()

        if not people_exists:
            adiciona_erro('Pessoa não localizada!')
            valid = False