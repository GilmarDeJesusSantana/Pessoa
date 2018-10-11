from django.conf.urls import url
from pessoa.views import index, cadastro_pessoa
urlpatterns = [
   url(r'^$',index,name = 'index'),
   url(r'^cadastro_pessoa/$',cadastro_pessoa, name='cadastro_pessoa'),
]
