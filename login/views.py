from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'login.html')

def usuarios(request):
    return render(request,'usuario.html')