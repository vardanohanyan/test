from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    sizechoices = (
        ('xsmall', 'xs'),
        ('small', 's'),
        ('medium', 'm'),
        ('large', 'l'),
        ('xlarge', 'xl')
    )
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    # discount_price = models.IntegerField()
    size = models.CharField(max_length=20, choices=sizechoices)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='user')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item')
    ordered = models.BooleanField(default=False)
    quanity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quanity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

