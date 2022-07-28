from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from trade.models import Wire, Trade
from trade.serializers import BalanceSerializer
from users.models import Profile
from django.db.models import F
from collections import Counter
from django.db.models.functions import Coalesce

from users.serializers import ProfileSerializer


@api_view(['GET'])
def index_view(request):
    # Just a test right here for homepage
    data = {"test": "Get data in JSON format", "success": True}
    return Response(data)


user_response = openapi.Response('response description', ProfileSerializer)


@swagger_auto_schema(methods=['get'],
                     operation_description="You can see your current balance without the open price calculate",
                     responses={200: user_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index_balance(request):
    default_balance = {"balance": 0.00}
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'), 0.00))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(
        balance=Coalesce(Sum((F('close_price') - F('open_price')) * F('quantity')), 0.00))
    open_price = Trade.objects.filter(profile_id=request.user, open=True).aggregate(
        balance=Coalesce(Sum(F('open_price') * F('quantity')), 0.00))
    profile = Profile.objects.filter(id=request.user.id).values('id', 'username', 'email', 'first_name', 'last_name',
                                                                'adress').first()

    if wire_total['balance'] == 0.00 and trade_price['balance'] == 0.00 or wire_total['balance'] + trade_price[
        'balance'] - open_price['balance'] == 0.00:
        profile.update(default_balance)
        return Response(profile)
    else:
        balance = dict(Counter(wire_total) + Counter(trade_price) - Counter(open_price))
        print(balance)
        profile.update(balance)
        return Response(profile)
