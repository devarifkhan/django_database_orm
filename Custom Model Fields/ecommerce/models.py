from django.db import models
from .fields import ProductIDField, OrderField, HexColorField

class Product(models.Model):
    name = models.CharField(max_length=10)
    productid = ProductIDField()
    order = OrderField()
    colour = HexColorField()

class Category(models.Model):
    name = models.CharField(max_length=10)
