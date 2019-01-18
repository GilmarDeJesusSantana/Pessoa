from django.conf.urls import url
from pessoa.views import index, CadastroPessoaView, PeopleSearch, PeopleDetails
urlpatterns = [
   url(r'^$',index,name = 'index'),
   url(r'^cadastro_pessoa/$',CadastroPessoaView.as_view(), name='cadastro_pessoa'),
   url(r'^pessoa_search/$',PeopleSearch.as_view(),name='pessoa_search'),
   url(r'^details/(?P<pessoa_id>\d+)$',PeopleDetails.as_view(),name='details'),
]
