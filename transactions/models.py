import uuid
from django.db import models
from base.models import BaseModel


class PaymentType(BaseModel):
    name = models.CharField(max_length=50)


class Gateway(BaseModel):
    name = models.CharField(max_length=50)
    accept_payments_types = models.ManyToManyField(PaymentType)


class Transaction(BaseModel):

    QUEUED = 1
    PROCESSED = 2
    CONCILITED = 3
    CANCELED = 4
    REFUNDED = 5

    STATUS = (
        (QUEUED, 'Queued'),
        (PROCESSED, 'Processed'),
        (CONCILITED, 'Concilited'),
        (CANCELED, 'Canceled'),
        (REFUNDED, 'Refunded'),
    ) 

    uuid = models.CharField(max_length=50, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=50)
    card_token = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=9)
    payment_type = models.OneToOneField(PaymentType, on_delete=models.PROTECT)
    gateway = models.ForeignKey(Gateway, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=STATUS)

    def __str__(self):
        return super().__str__()

    def execute_transaction(self):
        return
    
    def refund_transaction(self):
        return 
