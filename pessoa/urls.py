from django.conf.urls import url
from pessoa.views import index, CadastroPessoaView
urlpatterns = [
   url(r'^$',index,name = 'index'),
   url(r'^cadastro_pessoa/$',CadastroPessoaView.as_view(), name='cadastro_pessoa'),
]
