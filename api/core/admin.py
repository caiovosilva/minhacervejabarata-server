from django.contrib import admin
from .models import Estabelecimento
from .models import Cliente

admin.site.register(Cliente)
admin.site.register(Estabelecimento)
# Register your models here.
