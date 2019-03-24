from rest_framework import serializers
from .models import Estabelecimento, Marca, Tipo, Produto, Cesta, ItemCesta

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome', 'endereco')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome')

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'descricao', 'ml')

class ProdutoSerializer(serializers.ModelSerializer):
    estabelecimento = serializers.RelatedField(source='estabelecimento', read_only=True)
    marca = serializers.RelatedField(source='marca', read_only=True)
    tipo = serializers.RelatedField(source='tipo', read_only=True)

    class Meta:
        model = Produto
        fields = ('id', 'valor', 'estabelecimento','marca','tipo')

class CestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cesta
        fields = ('id', 'nome', 'data')

class ItemCestaSerializer(serializers.ModelSerializer):
    produto = serializers.RelatedField(source='produto', read_only=True)
    cesta = serializers.RelatedField(source='cesta', read_only=True)

    class Meta:
        model = Produto
        fields = ('id', 'valor', 'produto','cesta')
