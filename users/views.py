
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import users
from .serializers import usersSerializer


# Create your views here.



@api_view(['POST'])
def create_user(request):
    serializer=usersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

   


