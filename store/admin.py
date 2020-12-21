from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from store.models import Product, Categorias, Secciones, Images, Talles
from store.resource import ImagesResource, TallesResource
from django.db.models import Count, Max
from django.core.management.color import no_style
from django.db import connection


admin.site.site_header = "HidraSport Admin"

#inlines

class ImagesAdmin(admin.TabularInline):
    model = Images

class TallesAdmin(admin.TabularInline):
    model = Talles
        
    
#admin registers

class SeccionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categorias", "imagen")    
    pass

class CategoriastAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    
    list_display = ("id", "name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color', "image",)
    list_filter = ("name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color', "image",)
    inlines = [ImagesAdmin, TallesAdmin]
    actions = ['remover_duplicados', 'popular_productos']
    
    def popular_productos(self, request, queryset):
        tallesACrear = (
        Product.objects.all()
        )
        
        for talle in tallesACrear:
            t = Talles(product = Product.objects.get(id=talle.id), talle = "m")
            t.save()
        #t = Talles(product= Product.objects.get(id=self.id), talle = "m")
        #t.save()
        
        
    
    def remover_duplicados(self, request, queryset):
        unique_fields = ['name', 'descripcion','sexo', 'color', 'guard', 'diseño', 'detalle_color']

        duplicates = (
        Product.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
        )

        for duplicate in duplicates:
            (
                Product.objects
                .filter(**{x: duplicate[x] for x in unique_fields})
                .exclude(id=duplicate['max_id'])
                .delete()
            )
    
    
    #def lista_categorias(self, obj):
    #    return ", ".join([str(p) for p in #obj.categorias.all()])


@admin.register(Talles)
class TallesAdmin(ImportExportModelAdmin):
    #resource_class = TallesResource
    list_display = ('get_pk', 'get_name', 'id', 'product', 'talle', 'cantidad')
    
    def get_name(self, obj):
        return obj.product.name
    
    def get_pk(self, obj):
        return obj.product.pk
    
    


@admin.register(Images)
class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource
    pass


admin.site.register(Categorias, CategoriastAdmin)
admin.site.register(Secciones, SeccionesAdmin)

#---------- admin actions



