from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from store.models import Product, Categorias, Secciones, Images, Talles, Importar, Subcategorias, SubCatCol
from store.resource import ImagesResource, TallesResource
from django.db.models import Count, Max
from django.core.management.color import no_style
from django.db import connection
from django.db.models import Q

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

class SubCatColAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass

class CategoriastAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass

class SubcategoriasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destacada")
    pass


@admin.register(Importar)
class ImportarAdmin(ImportExportModelAdmin):
    
    list_display = ("id", 'codigo','subcodigo',"name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color', 'talle', 'cantidad')
    
    actions = ['completar_productos_y_talles', 'delete_all']
    
    
    
    def delete_all(self, request, queryset):
        while Importar.objects.count():
            ids = Importar.objects.values_list('pk', flat=True)[:500]
            Importar.objects.filter(pk__in = ids).delete()
    
    def completar_productos_y_talles(self, request, queryset):
        imported = (
        Importar.objects.all()
        )
        
        for imp in imported:
            
            
            
            if Product.objects.filter(codigo__contains = imp.codigo):     
                z = Product.objects.all().get(codigo = imp.codigo)
                t = Talles.objects.filter(Q(talle = imp.talle) & Q(codigo = imp.codigo))
                if len(t)<1:
                    
                    
                    t = Talles(product = Product.objects.get(id=z.id), talle = imp.talle, codigo = imp.codigo, subcodigo = imp.subcodigo, largo = imp.largo, cadera = imp.cadera, manga = imp.manga, siza = imp.siza, tiro = imp.tiro, bajo_busto = imp.bajo_busto, cintura = imp.cintura, cantidad =imp.cantidad)
                    t.save()
                    
            else:
                p = Product(name = imp.name, codigo = imp.codigo, price = imp.price, descripcion = imp.descripcion , sexo = imp.sexo, color = imp.color, guard = imp.guard, telas = imp.telas, diseño = imp.diseño, detalle_color = imp.detalle_color)
                p.save()
                t = Talles(product = Product.objects.get(id=p.id), talle = imp.talle, codigo = imp.codigo, subcodigo = imp.subcodigo, largo = imp.largo, cadera = imp.cadera, manga = imp.manga, siza = imp.siza, tiro = imp.tiro, bajo_busto = imp.bajo_busto, cintura = imp.cintura, cantidad =imp.cantidad)
                t.save()
            
            

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    
    list_display = ("id", 'codigo', "name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color',)
    list_filter = ("name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color',)
    inlines = [ImagesAdmin, TallesAdmin]
    
    #actions = ['remover_duplicados', 'popular_productos']
    
    class Media:
        js = ['main.js']
    
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
admin.site.register(Subcategorias, SubcategoriasAdmin)
admin.site.register(SubCatCol, SubCatColAdmin)
admin.site.register(Secciones, SeccionesAdmin)

#---------- admin actions



