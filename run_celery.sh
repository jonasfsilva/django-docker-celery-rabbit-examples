#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

celery -A payment_manager worker  -B -Q celery,transactions -l info
