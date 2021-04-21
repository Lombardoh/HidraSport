from django.shortcuts import render, redirect
from .models import Order, ProductsInOrder
from store.models import Product
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from cart.cart import Cart
# Create your views here.
@login_required
def checkout(request):
    
    user = request.user
    cart = request.session.get('cart')
    
    o = Order.objects.create(user=user)    
    
    
    for key, value in cart.items():
        print(key)
        print(value['userid'])
        ProductsInOrder.objects.create(order=Order.objects.all().get(id = o.id), product = Product.objects.all().get(id = key))
    
    cart = Cart(request)
    cart.clear()
        
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
