from django.contrib import admin

# Register your models here.
from .models import Order, ProductsInOrder

class ProductsInOrderAdmin(admin.TabularInline):
    model = ProductsInOrder
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user","totalPrice",)   
    inlines = [ProductsInOrderAdmin,]
    pass



admin.site.register(Order, OrderAdmin)
