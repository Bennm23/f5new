from django.db import models
from ckeditor.fields import RichTextField
from .constants import CATEGORY_CHOICES, MATERIAL_CHOICES

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    materials = models.CharField(max_length=255, choices=MATERIAL_CHOICES)

    def __str__(self):
        return self.name
