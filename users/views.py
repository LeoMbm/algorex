
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from trade.models import Wire, Trade
from users.models import Profile
from django.db.models import F
from collections import Counter
from django.db.models.functions import Coalesce
@api_view(['GET'])
def index_view(request):
    # Just a test right here for homepage
    data = {"test": "Get data in JSON format", "success": True}
    return Response(data)




@api_view(['GET'])
def index_balance(request):
    default_balance = {"balance":0.00}
    wire_total = Wire.objects.filter(user_id=request.user).aggregate(balance=Coalesce(Sum('amount'),0.00))
    trade_price = Trade.objects.filter(profile_id=request.user).aggregate(balance=Coalesce(Sum((F('close_price') - F('open_price'))*F('quantity')), 0.00))
    open_price = Trade.objects.filter(profile_id=request.user,open=True).aggregate(balance=Coalesce(Sum(F('open_price') * F('quantity')), 0.00))
    profile=Profile.objects.filter(id=request.user.id).values('id','username','email','first_name','last_name','adress').first()

    if wire_total['balance'] == 0.00 and trade_price['balance'] == 0.00 or wire_total['balance'] + trade_price['balance'] == 0.00:
        profile.update(default_balance)
        return Response(profile)
    else:
        balance = dict(Counter(wire_total) + Counter(trade_price) - Counter(open_price))
        print(balance)
        profile.update(balance)
        return Response(profile)
