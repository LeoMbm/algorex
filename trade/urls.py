from django.urls import path

from trade.views import Trade
tr = Trade(requests)
urlpatterns = [
    path('open/', tr.trade_open, name='open-trade'),
    path('<str:symbol_name>/marketprice/', get_pricemarket, name='get_pricemarket'),
    path('all/cryptocurrency/', get_list_cryptocurrency, name='get_pricemarket'),
    path('<str:symbol>/price/', get_realtime_price, name='get_realtime_price'),
]
