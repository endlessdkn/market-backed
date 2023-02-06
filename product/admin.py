from django.contrib import admin
from product.models import *

#Declarar Modelos para el admin de Django
# Register your models here.
admin.site.register(categoria)
admin.site.register(producto)
