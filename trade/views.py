

import os

from django.template.defaulttags import url
import requests
from rest_framework.views import APIView
from rest_framework import viewsets
from twelvedata import TDClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from trade.models import Wire,Trade
from trade.serializers import  TradeSerializer, WireSerializer
from users.models import Profile
from django.db.models import F
from collections import Counter

key = "abe6a366922b4b7f87fc2c2fef7948a7"
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=key)


# class Trade(APIView):

# def __init__(self, request, **kwargs):
#     super().__init__(**kwargs)
#     self.requests = None

#Wire
@api_view(['POST'])
def create_wire(request):
    
    wire_total=Wire.objects.filter(user_id=request.user).aggregate(result=Sum('amount'))
    trade_price=Trade.objects.filter(profile_id=request.user).aggregate(result=Sum((F('close_price') - F('open_price'))*F('quantity')))
    balance=dict(Counter(wire_total)+Counter(trade_price))
    if balance['result'] <= 0:
       return Response({"message":"not enough money"})
    else:
      serializer = WireSerializer(data=request.data)

      if serializer.is_valid():
           serializer.save(user_id=request.user)
           return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def index_wire(request):
    wire=Wire.objects.filter(user_id=request.user)
    serializer=WireSerializer(wire,many=True)
    print(type(serializer))
    return Response(serializer.data)



@api_view(['GET'])
def index_balance(request):
    wire_total=Wire.objects.filter(user_id=request.user).aggregate(balance=Sum('amount'))
    trade_price=Trade.objects.filter(profile_id=request.user).aggregate(balance=Sum((F('close_price') - F('open_price'))*F('quantity')))
    profile=Profile.objects.filter(id=request.user.id).values('id','username','email','first_name','last_name','adress').first()
    balance=dict(Counter(wire_total)+Counter(trade_price))
    profile.update(balance)
    
    return Response(profile)

#trade
@api_view(['POST'])
def trade_open(request):
    serializer = TradeSerializer(data=request)
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


