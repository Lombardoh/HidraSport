from django.shortcuts import render, redirect
from .models import Order, ProductsInOrder
from store.models import Product, Categorias, Talles
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from register.models import Profile
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def checkout(request):
    if str(request.user) == "AnonymousUser":
        
        return redirect("register")

    token = request.POST.get("token")
    payment_method_id = request.POST.get("payment_method_id")
    installments = request.POST.get("installments")
    issuer_id = request.POST.get("issuer_id")

    user = request.user
    cart = request.session.get('cart')
    profile = Profile.objects.get(id=user.id)
    total = 0
    o = Order.objects.create(user=user)    
    for key, value in cart.items():
       
        aux = Talles.objects.filter(talle=str(value['talle']))
        
        ProductsInOrder.objects.create(order=Order.objects.all().get(id = o.id), product = Product.objects.all().get(id = key), talle=aux[0].talle   )
        total += float(value['price']) * value['quantity']

    o.totalPrice = total
    o.direccionEntrega = profile.address
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

def test(request):
    return render(request, 'test.html', {})