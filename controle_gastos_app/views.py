from django.shortcuts import render
from django.db.models import Sum

from .models import Usuario
from .models import Transacao
from .models import Categoria

# Create your views here.
def home(request):
    data = {}
    data['usuario'] = Usuario.objects.all()
    data['transacoes'] = Transacao.objects.all()
    data['categoria'] = Categoria.objects.all()
    data['valorTotalEntrada'] = Transacao.objects.filter(tipo=1).aggregate(soma=Sum('valor'))['soma']
    data['valorTotalSaida'] = Transacao.objects.filter(tipo=2).aggregate(soma=Sum('valor'))['soma']
    data['total'] = data['valorTotalEntrada'] - data['valorTotalSaida']
    return render(request, 'home/home.html', data)
    

# def valorTotalEntrada(request):
#     soma_valores_entrada = Transacao.objects.filter(tipo=1).aggregate(soma=Sum('valor'))['soma']
#     return render(request, 'home/home.html', {'soma_valores_entrada': soma_valores_entrada})


# def valorTotalSaida(request):
#     soma_valores_saida = Transacao.objects.filter(tipo=2).aggregate(soma=Sum('valor'))['soma']
#     return render(request, 'home/home.html', {'soma_valores_saida': soma_valores_saida})