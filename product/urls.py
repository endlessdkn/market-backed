from rest_framework import routers

from django.urls import path
from product.views import *

router = routers.DefaultRouter()

#Rutas CRUD para Categoria y Producto
router.register('categoria', categoriaViewSet, 'categoria')
router.register('producto', productoViewSet, 'producto')

urlpatterns = router.urls