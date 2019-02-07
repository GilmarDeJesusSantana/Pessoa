from django.conf.urls import url
from login.views import index, CadastrarUsuario
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^usuarios/$',CadastrarUsuario.as_view(), name='usuarios')
]