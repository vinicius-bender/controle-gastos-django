from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from .models import Transacao


# Create your views here.
@login_required
def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.filter(iduser=request.user)
    
    data['valorTotalEntrada'] = Transacao.objects.filter(iduser=request.user, tipo=1).aggregate(soma=Sum('valor'))['soma']
    if (data['valorTotalEntrada'] is None):
        data['valorTotalEntrada'] = 0

    data['valorTotalSaida'] = Transacao.objects.filter(iduser=request.user, tipo=2).aggregate(soma=Sum('valor'))['soma']
    if (data['valorTotalSaida'] is None):
        data['valorTotalSaida'] = 0

    data['total'] = data['valorTotalEntrada'] - data['valorTotalSaida']
    
    return render(request, 'home/home.html', data)

class signup(generic.CreateView):
    form_class = UserCreationForm
    succes_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login')
    

def cadastrar_transacao(request):
    if request.method == 'POST':
        iduser = request.user
        titulo = request.POST['titulo']
        valor = request.POST['valor']
        categoria = request.POST['categoria']
        tipo = request.POST['tipo']

        transacao = Transacao(iduser=iduser, titulo=titulo, valor=valor, categoria=categoria, tipo=tipo)
        transacao.save()
    return redirect('/')

def remover_transacao(request, id):
    transacao = get_object_or_404(Transacao, pk=id)
    transacao.delete()
    return redirect('/')

def detalhes_transacao (request, id):
    detalhesTransacao = get_object_or_404(Transacao, pk=id)
    if request.method == 'POST':
        detalhesTransacao.titulo = request.POST['titulo']
        detalhesTransacao.valor = request.POST['valor']
        detalhesTransacao.categoria = request.POST['categoria']
        detalhesTransacao.tipo= request.POST['tipo']
        detalhesTransacao.save()
        return redirect('/')
    else:
        return render(request, 'editar/detalhes_transacao.html', {'detalhesTransacao': detalhesTransacao})

def listagem (request):
    return render(request, 'listagem/listagem.html')