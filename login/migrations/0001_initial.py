# Generated by Django 2.1 on 2019-01-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('perfil', models.CharField(max_length=10)),
            ],
        ),
    ]