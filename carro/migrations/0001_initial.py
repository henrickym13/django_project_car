# Generated by Django 4.2.5 on 2023-09-20 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('ano', models.IntegerField()),
                ('motor', models.CharField(max_length=20)),
                ('imagem', models.ImageField(upload_to='imagem_carro')),
                ('descricao', models.CharField(max_length=1500)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carro.marca')),
            ],
        ),
    ]
