from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from store.models import Product, Categorias, Secciones, Images


class SeccionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categorias", "imagen")    
    pass

class CategoriastAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass



class ImagesAdmin(admin.TabularInline):
    model = Images

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "created_on", "pk")
    inlines = [ImagesAdmin,]
    pass

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categorias, CategoriastAdmin)
admin.site.register(Secciones, SeccionesAdmin)