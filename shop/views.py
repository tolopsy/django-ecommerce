from django.shortcuts import render, get_object_or_404

from .models import Product, Category

# Create your views here.
def product_list(request, category_slug=None):
	products = Product.objects.filter(available=True)
	category = None
	categories = Category.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	context = {
		'products': products,
		'category': category,
		'categories': categories,
	}

	return render(request, 'index.html', context)


def product_detail(request, id, slug):
	product =  get_object_or_404(Product, id=id, slug=slug, available=True)
	context = {
		'product': product
	}
	return render(request, 'detail.html', context)