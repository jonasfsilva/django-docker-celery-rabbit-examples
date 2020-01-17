from django.shortcuts import render
from rest_framework import viewsets
from .models import Transaction
from .models import PaymentType
from .models import Gateway
from .serializers import TransactionSerializer
from .serializers import PaymentTypeSerializer
from .serializers import GatewaySerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
