from django.db import models

class Product(models.Model):
  CATEGORY_CHOICES = [
    ('apparel', 'Apparel'),
    ('caps', 'Caps'),
    ('teams', 'Teams'),
    ('players', 'Players'),
    ('short', 'Short sleeve'),
    ('long', 'Long sleeve'),
    ('shoes', 'Shoes'),
    ('accessories', 'Accessories'),
  ]

  MATERIAL_CHOICES = [
    ('cotton', 'Cotton'),
    ('leather', 'Leather'),
    ('polyester', 'Polyester'),
  ]
  
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  categories = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
  materials = models.CharField(max_length=255, choices=MATERIAL_CHOICES)

  def __str__(self):
      return self.name