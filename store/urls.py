from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("productos/<product>/", views.filtro, name="filtro"),
    path("<int:pk>", views.articulo_detalle, name="articulo_detalle"),
    path("product_list", views.product_list, name="product_list"),
    path("upload/<int:id>", views.file_upload_view, name="upload"),
]

#path("productos/<categoria>/", views.filtro, name="filtro"),