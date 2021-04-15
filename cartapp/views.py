from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponseRedirect
from store.models import Product, Categorias, Secciones

#@login_required(login_url="/users/login") uncomment to only allow authenticad users to use cart
def cart_add(request, id, talle):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product, talle=talle)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart_show(request):
    cart = Cart(request)
    cart.show()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

def cart_detail(request):
    destacadas=Categorias.objects.filter(destacada=True)
    
    context = {
        "destacadas": destacadas,
    }
    
    return render(request, 'cart_detail.html', context)