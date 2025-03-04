from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('continentes/<str:nome>/marcas/', views.exibir_marcas, name="exibir_marcas"),
    path('marcas/<slug:slug>/listar_carros/', views.listar_carros, name='listar_carros'),
    path('carro/<slug:slug>', views.exibir_carro, name="exibir_carro"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)