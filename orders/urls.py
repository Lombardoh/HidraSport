from django.urls import path
from . import views

urlpatterns = [
path("checkout/", views.checkout, name="checkout"),
path("test/", views.test, name='test'),
path("order_list/", views.order_list, name='order_list'),
]