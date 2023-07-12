# Generated by Django 4.2.2 on 2023-07-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_gastos_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tipo', models.IntegerField(max_length=1)),
                ('data', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_gastos_app.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='saidas',
            name='idusuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='total',
        ),
        migrations.DeleteModel(
            name='Entradas',
        ),
        migrations.DeleteModel(
            name='Saidas',
        ),
        migrations.AddField(
            model_name='transacao',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_gastos_app.usuario'),
        ),
    ]
