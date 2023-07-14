from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from .models import Transacao
from .models import Categoria


# Create your views here.
@login_required
def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.filter(iduser=request.user)
    data['categoria'] = Categoria.objects.all()
    
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