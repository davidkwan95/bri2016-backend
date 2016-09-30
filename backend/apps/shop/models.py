from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shop_name = models.CharField(max_length=30)

class Product(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    price = models.IntegerField()

class Order(models.Model):
    shop = models.ForeignKey(Shop)
    customer = models.ForeignKey(User)
    status = models.CharField(max_length=20)
    total_price = models.IntegerField(null = True)

class OrderLine(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_cost = models.IntegerField()
    line_price = models.IntegerField()