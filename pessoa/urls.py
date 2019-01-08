from django.conf.urls import url
from pessoa.views import index, CadastroPessoaView, pessoaSearch
urlpatterns = [
   url(r'^$',index,name = 'index'),
   url(r'^cadastro_pessoa/$',CadastroPessoaView.as_view(), name='cadastro_pessoa'),
   url(r'^pessoa_search/$',pessoaSearch.as_view(),name='pessoa_search'),
]
