from django.conf.urls import url
from login.views import Login, CadastrarUsuario
urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^usuarios/$',CadastrarUsuario.as_view(), name='usuarios')
]