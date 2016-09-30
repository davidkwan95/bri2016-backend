from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    shop = models.ForeignKey(Shop)
    customer = models.ForeignKey(User)
    status = models.CharField(max_length=20)
    total_price = models.IntegerField(null = True)
    created_at = models.DateField(auto_now_add = True, null = True)

class OrderLine(models.Model):
    order = models.ForeignKey(Order, related_name='lines')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_cost = models.IntegerField()
    line_price = models.IntegerField()