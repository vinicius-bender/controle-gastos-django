from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user

class Categoria(models.Model):
    categoria = models.TextField(max_length=50)

    def __str__(self):
        return self.categoria

class Transacao(models.Model):
    # idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.TextField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo