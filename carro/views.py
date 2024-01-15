from django.shortcuts import render
from .models import Carro, Continente, Marca


# Create your views here.
def listar_carros(request, slug):
    if request.method == "GET":
        marca = Marca.objects.get(slug=slug)
        carros = Carro.objects.filter(marca=marca)
        return render(request, 'listar_carros.html', {'carros': carros})


def exibir_carro(request, slug):
    if request.method == "GET":
        carro = Carro.objects.get(slug=slug)
        return render(request, 'carro.html', {'carro':carro})


def listar_continentes(request):
    if request.method == "GET":
        continentes = Continente.objects.all()
        return render(request, 'index.html', {'continentes': continentes})


def exibir_marcas(request, slug):
    if request.method == "GET":
        nome_continente = Continente.objects.get(slug=slug) 
        marcas = Marca.objects.filter(continente=nome_continente)
        return render(request, 'listar_marcas.html', {'marcas': marcas})


def navbar_marcas(request):
    if request.method == "GET":
        continentes = Continente.objects.all()
        return render(request, "base.html", {'continentes': continentes})