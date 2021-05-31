from django.shortcuts import render, redirect
from .models import Order, ProductsInOrder
from store.models import Product, Categorias, Talles
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from register.models import Profile
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def checkout(request, postal_code, delivery_type):
    if str(request.user) == "AnonymousUser":
        
        return redirect("register")

    token = request.POST.get("token")
    payment_method_id = request.POST.get("payment_method_id")
    installments = request.POST.get("installments")
    issuer_id = request.POST.get("issuer_id")

    costo = 0

    if (postal_code < 1441):
        costo= 450
    elif (postal_code > 1440 and postal_code < 2943 or postal_code > 6399 and postal_code < 8181):
        if delivery_type == "sucursal":
            costo = 750
        else:
            costo = 950
    else:
        if delivery_type == "sucursal":
            costo = 990
        else:
            costo = 1499


    user = request.user
    cart = request.session.get('cart')
    profile = Profile.objects.get(id=user.id)
    total = 0

    o = Order.objects.create(user=user,    
    products_cost = total,
    delivery_type = delivery_type,
    postal_code = postal_code,
    total_cost = total + postal_code,
    direccionEntrega = profile.address,
    delivery_cost = costo)

    for key, value in cart.items():
            
        ProductsInOrder.objects.create(order=Order.objects.all().get(id = o.id), 
        product = Product.objects.all().get(id = key), talle=value['talle'],
        subcodigo = value['subcodigo'], ubicacion = value['ubicacion'], tamaño_caja = value['tamaño_caja'])
        
        total += float(value['price']) * value['quantity']


    o.products_cost = total
    o.total_cost = total + costo
    o.save()
    cart = Cart(request)
    #cart.clear()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@staff_member_required
def order_list(request):

    orders = Order.objects.all()
    destacadas=Categorias.objects.filter(destacada=True)
    context = {
        "orders": orders,
        "destacadas": destacadas,
    }

    return render(request, 'order_list.html', context)

@staff_member_required
def order_build(request):
    orders = Order.objects.all()
    destacadas=Categorias.objects.filter(destacada=True)
    context = {
        "orders": orders,
        "destacadas": destacadas,
    }
    return render(request, 'order_build.html', context)