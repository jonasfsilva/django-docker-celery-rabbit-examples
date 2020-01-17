from django.conf import settings
from payment_manager.celery import app as celery_app
from celery import shared_task


@shared_task
def execute_trasactions(transaction):
    print('EXECUTE TRANSACTION')

@celery_app.task(queue='transactions')
def scheduled_task():
    print('SCHEDULED TASK')
