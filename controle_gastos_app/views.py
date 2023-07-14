from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from .models import Usuario
from .models import Transacao
from .models import Categoria


# Create your views here.
@login_required
def home(request):
    data = {}
    data['usuario'] = Usuario.objects.all()
    data['transacoes'] = Transacao.objects.all()
    data['categoria'] = Categoria.objects.all()
    data['valorTotalEntrada'] = Transacao.objects.filter(tipo=1).aggregate(soma=Sum('valor'))['soma']
    data['valorTotalSaida'] = Transacao.objects.filter(tipo=2).aggregate(soma=Sum('valor'))['soma']
    data['total'] = data['valorTotalEntrada'] - data['valorTotalSaida']
    return render(request, 'home/home.html', data)


class signup(generic.CreateView):
    form_class = UserCreationForm
    succes_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login')