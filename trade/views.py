import os
from django.db.models import ExpressionWrapper, FloatField
from django.db.models.functions import Coalesce
from django.template.defaulttags import url
import requests
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework import viewsets
from twelvedata import TDClient
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from trade.models import Wire, Trade
from trade.serializers import TradeSerializer, WireSerializer
from users.models import Profile
from django.db.models import F
from collections import Counter
from rest_framework.permissions import IsAuthenticated
key =os.getenv("MESSARI_KEY")
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=key)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_wire(request):

    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'),0.00))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(balance=Coalesce(Sum((F('close_price') - F('open_price')) * F('quantity')), 0.00))

    open_price = Trade.objects.filter(profile_id=request.user,open=True).aggregate(balance=Coalesce(Sum(F('open_price') * F('quantity')), 0.00))
    serializer = WireSerializer(data=request.data)
    amount = serializer.initial_data['amount']
    withdraw = serializer.initial_data['withdraw']
    if wire_total['balance']+trade_price['balance']-open_price['balance']-amount<0.00 and withdraw==True:
        data = {"message": "not enough money",}
        return Response(data)
    else:
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index_wire(request):
    wire = Wire.objects.filter(user_id=request.user)
    serializer = WireSerializer(wire, many=True)
    print(type(serializer))
    return Response(serializer.data)


# trade

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_trade(request):
    trade = Trade.objects.filter(profile_id=request.user)
    serializer = TradeSerializer(trade, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_open_trade(request):
    trade = Trade.objects.filter(profile_id=request.user, open=True)
    serializer = TradeSerializer(trade, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_close_trade(request):
    trade = Trade.objects.filter(profile_id=request.user, open=False)
    serializer = TradeSerializer(trade, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def closed_pnl(request):
    trade = Trade.objects.filter(profile_id=request.user).aggregate(
        PNL=Coalesce(Sum(F('close_price') * F('quantity')), 0.00))
    return Response(trade)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def open_pnl(request):
    trade = Trade.objects.filter(profile_id=request.user).aggregate(
        PNL=Coalesce(Sum(F('open_price') * F('quantity')), 0.00))
    return Response(trade)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_balance(request):
    default_balance = {"balance": 0.00}
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'), 0.00))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(
        balance=Coalesce(Sum((F('close_price') - F('open_price')) * F('quantity')), 0.00))
    if wire_total['balance'] == 0.00 and trade_price['balance'] == 0.00 or wire_total['balance'] + trade_price[
        'balance'] == 0.00:
        return Response(default_balance)
    else:
        balance = dict(Counter(wire_total) + Counter(trade_price))

        return Response(balance)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def trade_open(request):
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'),0.00))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(balance=Coalesce(Sum((F('close_price') - F('open_price'))* F('quantity')), 0.00))
    open_price = Trade.objects.filter(profile_id=request.user,open=True).aggregate(balance=Coalesce(Sum(F('open_price') * F('quantity')), 0.00))
    serializer = TradeSerializer(data=request.data)
    quantity = serializer.initial_data['quantity']
    symbol = serializer.initial_data['symbol']
    link = get_realtime_price(symbol)
    res_price = link.data['data']['market_data']['price_usd']
    res_symbol = link.data['data']['Asset']['symbol']
    print(res_price * quantity)
    if wire_total['balance'] + trade_price['balance'] - open_price['balance'] - (res_price*quantity) < 0.00:
        data = {"message": "not enough money",}
        return Response(data)
    else:
        if request.method == 'POST':

            if serializer.is_valid():
                serializer.save(profile_id=request.user, open_price=res_price)
                msg = {"You buy for": str(res_price * quantity) + " $" ,
                       "data": serializer.data}
                return Response(msg)
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
# TODO: Close a trade
def trade_close(request, trade_id):
    # FIXME: Try to get profit or loss in response
    trade = Trade.objects.get(id=trade_id, profile_id=request.user)
    tradeValue = Trade.objects.filter(id=trade_id, profile_id=request.user).values().first()
    if request.method == 'POST':
        link = get_realtime_price(trade.symbol)
        res = link.data['data']['market_data']['price_usd']
        pnl = (res - trade.open_price) * trade.quantity
        msg = {"message": "Trade Closed",
               "profit": str(pnl) + " $",
                "data": tradeValue}
        if trade.open is True:
            trade.open = False
            trade.close_datetime = now()
            trade.close_price = res
            trade.save()
            return Response(msg)
        elif trade.open is False:
            pnl = (trade.close_price - trade.open_price) * trade.quantity
            return Response({"message": "Trade already closed",
                             "data": tradeValue,
                              "profit": str(pnl) + " $",
                             })

# @api_view(['GET'])
def get_realtime_price(symbol):
    url = f'https://data.messari.io/api/v1/assets/{symbol}/metrics/market-data'
    res = requests.get(url).json()

    return Response(res)


@api_view(['GET'])
def get_list_cryptocurrency(request):
    url = 'https://data.messari.io/api/v2/assets'
    res = requests.get(url).json()

    return Response(res)
