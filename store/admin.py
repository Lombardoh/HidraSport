from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from store.models import Product, Categorias, Secciones, Images, Talles
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export import fields, resources

admin.site.site_header = "HidraSport Admin"

#inlines

class ImagesAdmin(admin.TabularInline):
    model = Images

class TallesAdmin(admin.TabularInline):
    model = Talles
        
#resources


class ImagesResource(resources.ModelResource):

    class Meta:
        model = Images
        fields = ('image', 'product__name')

class TallesResource(resources.ModelResource):

    class Meta:
        model = Talles
        fields = ('id',	'product__name', 'talle', 'product__id', 'cantidad',
)
    
#admin registers

class SeccionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categorias", "imagen")    
    pass

class CategoriastAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    #resource_class = ProductResource
    list_display = ('id', "name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color', "image")
    inlines = [ImagesAdmin, TallesAdmin]
    
    def lista_categorias(self, obj):
        return ", ".join([str(p) for p in obj.categorias.all()])
#    pass

@admin.register(Talles)
class TallesAdmin(ImportExportModelAdmin):
    resource_class = TallesResource
    pass

@admin.register(Images)
class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource
    pass


admin.site.register(Categorias, CategoriastAdmin)
admin.site.register(Secciones, SeccionesAdmin)
