from django.db import models
from shop.models import Product


class Order(models.Model):
	# Private Information
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=15)

	# Geographical Information
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=50)
	company = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.CharField(max_length=10)
	state = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True, default='Nigeria')

	# Delivery Method
	delivery_choices = (
		('pickup', 'Pickup'),
		('express', 'Oloja Express')
		)

	delivery_method = models.CharField(max_length=13, choices=delivery_choices, default='express')

	# Payment Method
	payment_choices = (
		('flutterwave', 'Flutterwave'),
		('paystack', 'Paystack'),
		('crypto', 'Crypto Pay'),
		('pay_on_delivery', 'Cash on delivery')
		)

	payment_method = models.CharField(max_length=20, choices=payment_choices, default='flutterwave')

	# Date and Time Information
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	paid = models.BooleanField(default=False) # Payment status

	def __str__(self):
		return 'Order %s' % self.id

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return 'order item %s' % self.id

	def get_cost(self):
		return self.price * self.quantity

