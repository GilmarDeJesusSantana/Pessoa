from django.conf.urls import url
from login.views import index, usuarios
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^usuarios/$',usuarios, name='usuarios')
]