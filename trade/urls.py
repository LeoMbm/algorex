from django.urls import path

from trade.views import trade_open, get_list_cryptocurrency, get_realtime_price, get_pricemarket

urlpatterns = [
    path('open/', trade_open, name='open-trade'),
    path('<str:symbol_name>/marketprice/', get_pricemarket, name='get_pricemarket'),
    path('all/cryptocurrency/', get_list_cryptocurrency, name='get_pricemarket'),
    path('<str:symbol>/price/', get_realtime_price, name='get_realtime_price'),
]
