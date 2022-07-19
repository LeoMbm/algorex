from dataclasses import field
from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.hashers import make_password



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name','last_name', 'password', 'adress']
    validate_password = make_password