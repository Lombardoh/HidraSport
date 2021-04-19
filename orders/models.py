from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product


# Create your models here.

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    direccionEntrega = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, blank=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, blank=True)
    