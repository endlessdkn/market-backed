from rest_framework import viewsets, permissions, authentication
from product.models import *
from product.serializers import *

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = categoriaSerializer

class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = productoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)