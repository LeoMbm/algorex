import requests
from django.urls import path

from trade.views import all_open_trade, all_close_trade, all_trade, closed_pnl, current_balance, \
    get_list_cryptocurrency, get_realtime_price, open_pnl, trade_open, create_wire, index_wire, trade_close

urlpatterns = [
    path('openTrade/', trade_open, name='open-trade'),
    path('<int:trade_id>/closeTrade/', trade_close, name='close-trade'),
    path('all/cryptocurrency/', get_list_cryptocurrency, name='get_pricemarket'),
    path('<str:symbol>/price/', get_realtime_price, name='get_realtime_price'),
    path('wire/', create_wire, name='wire_post'),
    path('wire_index/', index_wire, name='wire_index'),
    path('index/', all_trade),
    path('index/open/', all_open_trade),
    path('index/closed/', all_close_trade),
    path('closedPNL/', closed_pnl),
    path('openPNL/', open_pnl),
    path('currentBalance/', current_balance),
]
