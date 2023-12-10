# f5store/forms.py 

from django import forms
from .models import Product
from django.forms import ModelForm, widgets

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'thumbnail', 'quantity', 'description', 'price', 'categories', 'materials']
