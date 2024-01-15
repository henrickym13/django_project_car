from django.contrib import admin
from .models import Marca, Carro, Continente

# Register your models here.
admin.site.register(Carro)
admin.site.register(Marca)
admin.site.register(Continente)