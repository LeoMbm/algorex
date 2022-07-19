from dataclasses import field

from rest_framework import serializers

from users.models import users




class usersSerializer(serializers.ModelSerializer):
    class Meta:
        
        model=users
        fields=['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = users.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user