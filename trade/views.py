import os

import requests
from rest_framework.views import APIView
from twelvedata import TDClient
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Algorex.settings import env
from trade.serializers import TradeSerializer

key = "abe6a366922b4b7f87fc2c2fef7948a7"
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=key)


# TODO: Read about viewset
class Trade(APIView):
    @api_view(['POST'])
    def trade_open(request):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['GET'])
    def get_pricemarket(request, symbol_name):
        # Construct the necessary time series
        ts = td.time_series(
            symbol=symbol_name,
            interval="1min",
            outputsize=20,
        )
        return Response(ts.as_json())

    @api_view(['GET'])
    def get_realtime_price(request, symbol):
        url = f'https://api.twelvedata.com/price?symbol={symbol}&apikey={key}'
        res = requests.get(url).json()

        return Response(res)

    @api_view(['GET'])
    def get_list_cryptocurrency(request):
        url = 'https://api.twelvedata.com/cryptocurrencies'
        res = requests.get(url).json()

        return Response(res)
