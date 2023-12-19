from django.db import models
from ckeditor.fields import RichTextField

class LocalStripeProduct(models.Model):
    product_name = models.CharField(max_length=50)
    product_id = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.product_id
    
class Material(models.Model):
    name = models.CharField(max_length=50),
    percentage = models.PositiveIntegerField(default=0)
    # You can add more fields here if needed, like description, properties, etc.

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    # Optional: color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=50, default="https://i.imgur.com/pcq1IAz.jpeg")
    description = RichTextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    materials = models.ManyToManyField(Material)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

