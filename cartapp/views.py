from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponseRedirect
from store.models import Product, Categorias, Secciones
from register.models import Profile
from django.contrib import messages



#@login_required(login_url="/users/login") uncomment to only allow authenticad users to use cart
def cart_add(request, id, talle):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product, talle=talle)
    messages.success(request, "El producto fue agreagado al carrito")
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
    user = request.user
    profile = Profile.objects.get(id=user.id)
    cart = request.session.get('cart')
    total = 0
    address = profile.address
    for key, value in cart.items():
        total += float(value['price']) * value['quantity']

    context = {
        "destacadas": destacadas,
        "total": total,
        "address": address,
    }
    
    return render(request, 'cart_detail.html', context)