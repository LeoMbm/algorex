from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index_view(request):
    # Just a test right here for homepage
    data = {"test": "Get data in JSON format", "success": True}
    return Response(data)
