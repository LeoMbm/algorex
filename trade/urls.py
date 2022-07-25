import requests
from django.urls import path

from trade.views import get_list_cryptocurrency, get_realtime_price, index_balance, trade_open,create_wire,index_wire,index_balance

# Can't use Class here
# tr = Trade(requests)
urlpatterns = [
    path('open/', trade_open, name='open-trade'),
    path('all/cryptocurrency/', get_list_cryptocurrency, name='get_pricemarket'),
    path('<str:symbol>/price/', get_realtime_price, name='get_realtime_price'),
    path('wire/',create_wire,name='wire'),
    path('wire_index/',index_wire,name='wire'),
    path('profile/',index_balance,name='wire'),
]
