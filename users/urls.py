from django.urls import path
from users.views import *

#Directorio del Usuario
urlpatterns = [
    path('create', CreateUserView.as_view()),
    path('login', CreateTokenView.as_view()),
    path('logout', LogoutView.as_view()),
    path('data', RetreiveUpdateUserView.as_view()),
]
