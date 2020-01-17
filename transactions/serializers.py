from rest_framework import serializers
from .models import Transaction
from .models import PaymentType
from .models import Gateway


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
