from rest_framework import serializers

from trade.models import Trade, Wire


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = ('id', 'profile_id', 'open_price', 'close_price', 'open_datetime', 'close_datetime', 'open')


class WireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wire
        fields = '__all__'
        read_only_fields = ('id', 'user_id')


# Only for Swagger Docs ! Never used this class
class BalanceSerializer(serializers.Serializer):
    balance = serializers.FloatField(default=0.00)


# Only for Swagger Docs ! Never used this class
class PNLSerializer(serializers.Serializer):
    PNL = serializers.FloatField(default=0.00)
