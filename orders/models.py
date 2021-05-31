from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product
from enum import Enum

# Create your models here.

User = get_user_model()

class Order(models.Model):

    PENDING = 'Pendiente'
    READY = 'Armado'
    DISPATCHED = 'Enviado'
    RECEIVED = 'Recibido'
    CLOSED = 'Cerrado'

    CHOICES = (
        (PENDING, PENDING),
        (READY, READY),
        (DISPATCHED, DISPATCHED),
        (RECEIVED, RECEIVED),
        (CLOSED, CLOSED),
    )

    status = models.CharField(max_length=255, choices=CHOICES, default=PENDING)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    direccionEntrega = models.TextField(max_length=70, )
    timestamp = models.DateTimeField(auto_now_add=True)
    postal_code = models.IntegerField()
    delivery_type = models.CharField(max_length=30)
    delivery_cost = models.IntegerField()
    products_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class ProductsInOrder(models.Model):
    subcodigo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    tamaño_caja = models.CharField(max_length=50, blank=True, null=True)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, blank=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, blank=True)
    talle = models.CharField(max_length=20)
    
    