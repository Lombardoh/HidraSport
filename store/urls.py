from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("productos/<categoria>/", views.filtro, name="filtro"),
    path("<int:pk>", views.articulo_detalle, name="articulo_detalle"),
]