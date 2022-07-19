from dataclasses import field
from rest_framework import serializers
from users.models import users
from django.contrib.auth.hashers import make_password



class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=['username','email','first_name','last_name','password','adress']
    validate_password = make_password