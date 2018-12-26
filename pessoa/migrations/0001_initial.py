# Generated by Django 2.1.2 on 2018-10-04 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=8)),
                ('bloco', models.CharField(max_length=3)),
                ('apartamento', models.CharField(max_length=4)),
                ('complemento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('flag_delete', models.CharField(max_length=1)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Endereco')),
            ],
        ),
    ]