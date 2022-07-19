from django.urls import path

from trade.views import trade_open, get_pricemarket

urlpatterns = [
    path('open/', trade_open, name='open-trade'),
    path('all/', get_pricemarket, name='all_pricemarket'),
]
