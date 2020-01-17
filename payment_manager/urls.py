from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from transactions.views import TransactionViewSet
from transactions.views import PaymentTypeViewSet
from transactions.views import GatewayViewSet

router = routers.DefaultRouter()
router.register(r'payment-types', PaymentTypeViewSet)
router.register(r'gateways', GatewayViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
