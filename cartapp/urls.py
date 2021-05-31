from django.urls import path
from . import views


urlpatterns = [
    #path('add/<int:id>/', views.cart_add, name='cart_add'),
    
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart_detail/', views.cart_detail,name='cart_detail'),
    path('cart_show', views.cart_show, name='cart_show'),
    
    path(
        'add/<int:id>/',
        views.cart_add, 
        name='cart_add'
    ),
    path(
        'add/<int:id>/<str:talle>/',
        views.cart_add,
        name='cart_add'
    ),

    path(
        'item_increment/<int:id>/',
        views.item_increment, 
        name='item_increment'
    ),
    path(
        'item_increment/<int:id>/<str:talle>/',
        views.item_increment,
        name='item_increment'
    ),
]