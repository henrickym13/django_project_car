from django.shortcuts import render
from .models import Carro, Continente, Marca
from django.core.paginator import Paginator


# Create your views here.
def listar_carros(request, slug):
    if request.method == "GET":
        marca = Marca.objects.get(slug=slug)
        carros = Carro.objects.filter(marca=marca)
        carros_pg = Paginator(carros, 9)

        page_number = request.GET.get('page')
        page_obj = carros_pg.get_page(page_number)
        return render(request, 'listar_carros.html', {'page_obj': page_obj})


def exibir_carro(request, slug):
    if request.method == "GET":
        carro = Carro.objects.get(slug=slug)
        return render(request, 'carro.html', {'carro':carro})


def exibir_marcas(request, nome):
    if request.method == "GET":
        nome_continente = Continente.objects.get(nome=nome) 
        marcas = Marca.objects.filter(continente=nome_continente)
        marcas_pg = Paginator(marcas, 9)

        page_number = request.GET.get('page')
        page_obj = marcas_pg.get_page(page_number)
        return render(request, 'listar_marcas.html', {'page_obj': page_obj})
