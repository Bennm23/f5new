from .models import Product

from django.forms import ModelForm, widgets

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'price', 'categories', 'materials']