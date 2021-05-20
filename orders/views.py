from django.shortcuts import render, redirect
from .models import Order, ProductsInOrder
from store.models import Product
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from cart.cart import Cart

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
    
    o = Order.objects.create(user=user)    
    for key, value in cart.items():
        print(key)
        print(value['userid'])
        ProductsInOrder.objects.create(order=Order.objects.all().get(id = o.id), product = Product.objects.all().get(id = key))
    
    cart = Cart(request)
    cart.clear()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def process_payment(request):
    pass
#     token = request.POST.get("token")
#     payment_method_id = request.POST.get("payment_method_id")
#     installments = request.POST.get("installments")
#     issuer_id = request.POST.get("issuer_id")
#     return render(request, 'process_payment.html', {})

def test(request):
    return render(request, 'test.html', {})