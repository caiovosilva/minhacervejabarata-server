from django.contrib import admin
from .models import Estabelecimento, Marca, Tipo, Produto, Cesta, ItemCesta

admin.site.register(Estabelecimento)
admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Produto)
admin.site.register(Cesta)
admin.site.register(ItemCesta)
