import requests
from django.urls import path

from trade.views import get_pricemarket, get_list_cryptocurrency, get_realtime_price, trade_open

# Can't use Class here
# tr = Trade(requests)
urlpatterns = [
    path('open/', trade_open, name='open-trade'),
    path('<str:symbol_name>/marketprice/', get_pricemarket, name='get_pricemarket'),
    path('all/cryptocurrency/', get_list_cryptocurrency, name='get_pricemarket'),
    path('<str:symbol>/price/', get_realtime_price, name='get_realtime_price'),
]
