from django.urls import path
from . import views

urlpatterns = [
path('checkout/<int:postal_code>/<str:delivery_type>', views.checkout, name="checkout"),
path("order_build/", views.order_build, name='order_build'),
path("order_list/", views.order_list, name='order_list'),
]