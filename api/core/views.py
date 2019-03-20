from django.shortcuts import render
from rest_framework import viewsets
from .models import Estabelecimento,Cliente
from .serializers import EstabelecimentoSerializer, ClienteSerializer



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
