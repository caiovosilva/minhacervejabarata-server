"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from core.views import EstabelecimentoViewSet, MarcaViewSet, TipoViewSet, ProdutoViewSet, CestaViewSet, ItemCestaViewSet

router = routers.DefaultRouter()
router.register(r'estabelecimentos', EstabelecimentoViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'tipos', TipoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'cestas', CestaViewSet)
router.register(r'itenscesta', ItemCestaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
