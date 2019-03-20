from rest_framework import serializers
from .models import Estabelecimento, Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco','idade')

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome', 'endereco')
