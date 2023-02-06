from django.db import models
from django.conf import settings

# Create your models here.
#Modelo Categoria
class categoria(models.Model):
    Categoria = models.CharField(max_length=250, verbose_name='Categoria')
    Descripcion = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.Categoria

    class Meta:
        db_table = 'categoria'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

#Modelo Producto con Llaves foraneas para la categoria y el Usuario que inicia sesion
class producto(models.Model):
    departamento = models.ForeignKey('Categoria', related_name='categoria_dep', on_delete=models.CASCADE, verbose_name='Categoria')
    item = models.CharField(max_length=250, verbose_name='Producto')
    precio = models.IntegerField(verbose_name='Precio')
    cant = models.IntegerField(verbose_name='Existencia')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    def __str__(self):
        return '{} - {}' .format(self.item, self.departamento)

    class Meta:
        db_table = 'producto'
        managed = True
        verbose_name = 'producto'
        verbose_name_plural = 'productos'