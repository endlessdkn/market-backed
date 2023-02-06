from django.contrib import admin
from users.models import User

# registrar el modelo de usuario
admin.site.register(User)
