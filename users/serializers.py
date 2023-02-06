from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

#Serializador de los datos de Usuarios
class UserSerializer(serializers.ModelSerializer):
    #Mostrar Datos del Usuario
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password' : {'write_only': True}}
    
    #Crear Usuario
    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)

    #Actualizar Usuario
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

#Generar Token de Autentificacion
class AuthTokenSerializer(serializers.Serializer):
    #Pedir datos de Inicio de Sesión
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    #Validar datos
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            raise serializers.ValidationError('No se realizo autentificacion', code='authorization')
        
        data['user'] = user
        return data