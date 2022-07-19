from django.urls import path, include

from users.views import create_user

urlpatterns = [
    path('register/', create_user, name='register' ),


]
