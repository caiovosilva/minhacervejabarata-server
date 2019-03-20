from django.shortcuts import render
from rest_framework import viewsets
from .models import Estabelecimento, Marca, Tipo, Produto, Cesta, ItemCesta
from .serializers import EstabelecimentoSerializer, MarcaSerializer, TipoSerializer, ProdutoSerializer, CestaSerializer, ItemCestaSerializer


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
class CestaViewSet(viewsets.ModelViewSet):
    queryset = Cesta.objects.all()
    serializer_class = CestaSerializer
class ItemCestaViewSet(viewsets.ModelViewSet):
    queryset = ItemCesta.objects.all()
    serializer_class = ItemCestaSerializer
