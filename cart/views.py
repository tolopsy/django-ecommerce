from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	if request.POST:
		form = CartAddProductForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
	else:
		cart.add(product=product) 

	return redirect('cart:cart_detail')


def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
	context = {
		'cart': cart
	}
	return render(request, 'cart_detail.html', context)