from django.shortcuts import render
from .people import PeopleDetails, PeopleSearch, CadastroPessoaView

def index(request):
    return render(request,'index.html')

CadastroPessoaView()

PeopleSearch()

PeopleDetails()




