from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    sort_order = models.IntegerField(default=0)

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='products/images/')
    caption = models.CharField(max_length=255)
    sort_order = models.IntegerField(default=0)

class Parameter(models.Model):
    product = models.ForeignKey(Product, related_name='parameters', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sort_order = models.IntegerField(default=0)
