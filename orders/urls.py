from django.urls import path
from . import views

urlpatterns = [
path("checkout/", views.checkout, name="checkout"),
path("test/", views.test, name='test'),
path("process_payment/", views.process_payment, name='process_payment'),
]