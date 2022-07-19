from rest_framework import serializers

from trade.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'profile_id','symbol', 'quantity', 'open_price', 'close_price', 'open_datetime', 'close_datetime', 'open')
