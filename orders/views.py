from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from cart.cart import Cart
from .models import OrderItem, Order
from .forms import CheckoutForm
from .tasks import order_mail

import weasyprint



# Create your views here.
def checkout(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = CheckoutForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'], 
										 price=item['price'], quantity=item['quantity'])
			cart.clear()
			context = {'order': order, 'cart': cart}
			order_mail.delay(order.id)
			return render(request, 'order_review.html', context)

	else:
		form = CheckoutForm()
		context  = {'cart': cart, 'form': form}

		return render(request, 'checkout.html', context)


@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'staff/order_detail.html', {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('order_pdf.html', {'order':order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)

	weasyprint.HTML(string=html).write_pdf(response)
	return response