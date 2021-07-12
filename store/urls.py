from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("productos/<product>/", views.filtro, name="filtro"),
    path("<int:pk>", views.articulo_detalle, name="articulo_detalle"),
    path("product_list/<str:name>/", views.product_list, name="product_list"),
    path("productos/upload/<int:id>", views.file_upload_view, name="upload"),
    path("productos/delete/<int:id>", views.file_delete_view, name="delete"),
]

#path("productos/<categoria>/", views.filtro, name="filtro"),