from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class  Product(models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    path = models.ImageField(upload_to="imagens/")

class User(models.Model):
    name = models.CharField(max_length=240)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()