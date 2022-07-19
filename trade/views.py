import os

import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Algorex.settings import env
from trade.serializers import TradeSerializer


@api_view(['POST'])
def trade_open(request):
    serializer = TradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_pricemarket(request):
    key = 'mQdoYVZswlthedMwY1AH'
    url = 'https://marketdata.tradermade.com/api/v1/live?'
    querystring = {"currency": "USDJPY", "api_key": key}
    response = requests.get(url, params=querystring)
    return Response(response)

