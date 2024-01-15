from django.shortcuts import render
from carro.models import Continente, Carro

def index(request):
    if request.method == "GET":
        continentes = Continente.objects.all()
        carros = Carro.objects.all()
        return render(request, 'index.html', {'continentes': continentes, 'carros':carros})
