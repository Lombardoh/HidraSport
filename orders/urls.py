from django.urls import path
from . import views

urlpatterns = [
path("test", views.order_checkout_view, name="order_checkout_view"),
]