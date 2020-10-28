from django import forms



class CartAddProductForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)