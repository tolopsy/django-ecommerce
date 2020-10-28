from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='First name')
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Last name')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='E-mail Address')
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Telephone')
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Address')
	city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='City')
	zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='ZIP code')
	state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='State')

	delivery_method = forms.CharField(required=True)
	payment_method = forms.CharField(required=True)
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city',
				  'zip_code', 'state', 'delivery_method', 'payment_method']

	# quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)