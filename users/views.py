from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import User

# Create your views here.

#crear Usuario
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

#Ver Usuario y Actualizar Usuario
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

#Crear Token
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

#Lista
class ListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#Cerrar Sesion y eliminar token
class LogoutView(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Sesión cerrada exitosamente."})