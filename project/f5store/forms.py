# f5store/forms.py 

from django import forms
from .models import Product
from django.forms import ModelForm, widgets
from .constants import CATEGORY_CHOICES, MATERIAL_CHOICES

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    category = forms.ChoiceField(choices=Product.CATEGORY_CHOICES, required=False)
    material = forms.ChoiceField(choices=Product.MATERIAL_CHOICES, required=False)
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'price', 'categories', 'materials']
