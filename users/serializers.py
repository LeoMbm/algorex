from rest_framework import serializers
from users.models import Profile
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer





class CustomRegisterSerializer(RegisterSerializer):
    adress = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['adress'] = self.validated_data.get('adress', '')
        data_dict['username'] = self.validated_data.get('username', '')
        
        return data_dict




class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    class Meta(UserDetailsSerializer.Meta):
        fields =('pk','username','email','first_name','last_name','adress',)
        read_only_fields=('pk','username',)


# Only for Swagger Docs ! Never used this class
class ProfileSerializer(serializers.Serializer):
    id = serializers.FloatField(default=0.00)
    username = serializers.CharField(default="algorex")
    email = serializers.CharField(default="algorex@me.com")
    first_name = serializers.CharField(default="Drew")
    last_name = serializers.CharField(default="Wallace")
    adress = serializers.CharField(default="Brussels")
    balance = serializers.FloatField(default=0.00)