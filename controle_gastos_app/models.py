from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Categoria(models.Model):
    categoria = models.TextField(max_length=50)

    def __str__(self):
        return self.categoria

class Transacao(models.Model):
    iduser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.TextField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo