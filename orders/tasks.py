from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_mail(order_id):
	order = Order.objects.get(id=order_id)
	subject = 'Oloja market: Order number {}'.format(order_id)
	message = 'Good day, {}! You have successfully ordered from Oloja market.\nYour Order number is {}'.format(order.first_name, order.id)
	mailer = send_mail(subject, message, 'admin@oloja.com', ['order.email'])
	return mailer

