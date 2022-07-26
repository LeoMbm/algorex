
import os
from django.db.models.functions import Coalesce
from django.template.defaulttags import url
import requests
from rest_framework.views import APIView
from rest_framework import viewsets
from twelvedata import TDClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from trade.models import Wire, Trade
from trade.serializers import TradeSerializer, WireSerializer
from users.models import Profile
from django.db.models import F
from collections import Counter

key = "abe6a366922b4b7f87fc2c2fef7948a7"
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=key)


# TODO: Read about viewset

# Wire
@api_view(['POST'])
def create_wire(request):
    # FIXME: I can withdraw below 0 but not after being below 0
    default_balance = {"balance": 0}
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'),0))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(balance=Coalesce(Sum((F('close_price') - F('open_price'))*F('quantity')), 0))
    balance = dict(Counter(wire_total) + Counter(trade_price))
    print(wire_total)
    serializer = WireSerializer(data=request.data)
    amount = serializer.initial_data['amount']
    withdraw = serializer.initial_data['withdraw']
    if wire_total['balance']+trade_price['balance']-amount<0 and withdraw==True:
        data = {"message": "not enough money",}
        return Response(data)
    else:
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data)
    return Response(serializer.errors)




@api_view(['GET'])
def index_wire(request):
    wire = Wire.objects.filter(user_id=request.user)
    serializer = WireSerializer(wire, many=True)
    print(type(serializer))
    return Response(serializer.data)




# trade

@api_view(['GET'])
def all_trade(request):
    trade= Trade.objects.filter(profile_id=request.user)
    serializer=TradeSerializer(trade,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_open_trade(request):
    trade= Trade.objects.filter(profile_id=request.user,open=True)
    serializer=TradeSerializer(trade,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_close_trade(request):
    trade= Trade.objects.filter(profile_id=request.user,open=False)
    serializer=TradeSerializer(trade,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def closed_pnl(request):
    trade= Trade.objects.filter(profile_id=request.user).aggregate(PNL=Coalesce(Sum(F('close_price')*F('quantity')),0))
    return Response(trade)  

@api_view(['GET'])
def open_pnl(request):
    trade= Trade.objects.filter(profile_id=request.user).aggregate(PNL=Coalesce(Sum(F('open_price')*F('quantity')),0))
    return Response(trade)

@api_view(['GET'])
def current_balance(request):
    default_balance = {"balance":0}
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'),0))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(balance=Coalesce(Sum((F('close_price') - F('open_price'))*F('quantity')), 0))
    
    if wire_total['balance'] ==0 and trade_price['balance'] == 0 or wire_total['balance'] + trade_price['balance'] == 0 :
        return Response(default_balance)
    else:
        balance = dict(Counter(wire_total) + Counter(trade_price))
        
        return Response(balance)

#jeremy
@api_view(['POST'])
def trade_open(request):
    serializer = TradeSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_realtime_price(request, symbol):
    url = f'https://data.messari.io/api/v1/assets/{symbol}/metrics/market-data'
    res = requests.get(url).json()

    return Response(res)

@api_view(['GET'])
def get_list_cryptocurrency(request):
    # TODO: Use Messari API
    url = 'https://data.messari.io/api/v2/assets'
    res = requests.get(url).json()

    return Response(res)
