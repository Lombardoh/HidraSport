from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Talles
from django.db.models import Q



class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
            
    def add(self, product, talle='s', quantity=1, action=None):       
        
        id = product.id
        t = Talles.objects.all().get(Q(talle=talle) & Q(product__id=id))
        newItem = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.name,
                'descripcion': product.descripcion,
                'sexo': product.sexo,
                'color': product.color,
                'quantity': 1,
                'price': product.price,
                'codigo': product.codigo,
                'image': product.image.url,
                'talle': talle,
                'subcodigo': t.subcodigo,
                'ubicacion': t.ubicacion,
                'tamaño_caja': t.tamaño_caja,

            }
            
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    
                }
        

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")
                
    

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
