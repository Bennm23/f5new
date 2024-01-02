from django.db import models
from ckeditor.fields import RichTextField

class Material(models.Model):
    name = models.CharField(max_length=50, default='none')
    percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class Category(models.Model):
    name = models.CharField(max_length=50)
    # Optional: color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_product_desc = models.CharField(max_length=149, blank=True, null=True)
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

