from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all() # Busca todos os produtos do banco
    return render(request, 'app1/index.html', {'produtos': produtos})