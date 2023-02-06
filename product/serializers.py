from rest_framework import serializers
from product.models import *

#Serializador de Categoria
class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('id', 'Categoria','Descripcion')

#Serializador de Productos, con bloqueo de modificar fecha y usuario
class productoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = producto
        fields = ('id', 'departamento','item', 'precio', 'cant', 'usuario', 'creado')
        read_only_fields = ('usuario', 'creado')
