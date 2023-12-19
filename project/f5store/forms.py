# f5store/forms.py 

from django import forms
from .models import Category, Product, Material
from django.forms import CheckboxSelectMultiple, ModelForm, widgets

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)

class ProductForm(ModelForm):
	categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), 
                                              required=False,
                                              widget=CheckboxSelectMultiple, 
                                              blank=True)
	materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
											required=False,
											widget=CheckboxSelectMultiple,
											blank=True)
	class Meta:
		model = Product
		widgets = {
            'categories': CheckboxSelectMultiple(),
			'materials': CheckboxSelectMultiple(),
        }
		fields = ['name', 'thumbnail', 'quantity', 'description', 'price', 'categories', 'materials']
