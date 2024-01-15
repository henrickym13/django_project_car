from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Continente(models.Model):
    nome = models.CharField(max_length=15, unique=True)
    imagem = models.ImageField(upload_to="img_continentes")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        
        return super().save(*args, **kwargs)


class Marca(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    continente = models.ForeignKey(Continente, on_delete=models.SET_NULL, null=True)
    pais = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="logo_marca")
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        
        return super().save(*args, **kwargs)


class Carro(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    ano = models.IntegerField()
    motor = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="imagem_carro")
    descricao = models.CharField(max_length=1500)
    slug = models.SlugField(unique=True, blank=True, null=True)
    url_video = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        
        return super().save(*args, **kwargs)
    