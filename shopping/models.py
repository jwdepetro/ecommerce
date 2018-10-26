from django.db import models
from datetime import datetime

class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return 'Cart'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.item.name, self.qty)