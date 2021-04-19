from django.shortcuts import render, redirect
from .models import Order, ProductsInOrder
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from cart.cart import Cart
# Create your views here.
@login_required
def checkout(request):
    
    
        
    
    
    
    
    qs = Product.objects.filter(id=274)
    if not qs.exists():
        return redirect("/")
    product = qs.first()
    user = request.user
    
    p = ProductsInOrder(product = Product.objects.get(id=274))
    Order.objects.create(user=user)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
