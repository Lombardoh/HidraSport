from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from store.models import Product, Categorias, Secciones, Images, Talles, Importar, Subcategorias, SubCatCol
from store.resource import ImagesResource, TallesResource
from django.db.models import Count, Max
from django.core.management.color import no_style
from django.db import connection
from django.db.models import Q
import os

admin.site.site_header = "HidraSport Admin"

#inlines

class ImagesAdmin(admin.TabularInline):
    model = Images

class TallesAdmin(admin.TabularInline):
    model = Talles
            
class SubCatColInline(admin.TabularInline):
    model = SubCatCol

class SubcategoriasInline(admin.TabularInline):
    model = Subcategorias

#admin registers

class SeccionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categorias", "imagen")    
    pass

@admin.register(Categorias)
class CategoriastAdmin(ImportExportModelAdmin):
    list_display = ("id", "nombre", "destacada")
    inlines =[SubCatColInline]
    pass

@admin.register(SubCatCol)
class SubCatColAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nombre", "destacada", "id")
    inlines = [SubcategoriasInline]

@admin.register(Subcategorias)
class SubcategoriasAdmin(admin.ModelAdmin):
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
    
    list_display = ("id", 'codigo', "name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color', 'image', 'secundaria')
    list_filter = ("name", "descripcion", "sexo", "color", "guard", "telas", "diseño", 'detalle_color',)
    inlines = [ImagesAdmin, TallesAdmin]
    
    actions = ['asociar_imagenes', 'fix_names']
    
    class Media:
        js = ['main.js']
    
    def fix_names(self, request, queryset):
        products = Product.objects.all()

        for p in products:
            p.name = p.name.replace('_', ' ')
            p.descripcion = p.descripcion.replace('_', ' ')
            p.color = p.color.replace('_', ' ')
            p.save()


    def asociar_imagenes(self, request, queryset):
        products = Product.objects.all()
        
        for p in products:
            
            aux = "products/" + p.name.lower() + "/" + p.descripcion + "_" + p.color
            


            if p.guard != "-":
                aux = aux + "_" + p.guard
            if p.diseño != "-":
                aux = aux + "_" + p.diseño
            if p.detalle_color != "-":
                aux = aux + "_" + p.detalle_color


            aux = aux.replace(' ', '_')
            

            if os.path.isfile("static/media/" + aux + "_FRENTE.png") == True:
                p.image = aux + "_FRENTE.png"
            elif os.path.isfile("static/media/" + aux + "_DORSO.png") == True:
                p.image = aux + "_DORSO.png"
            else:
                p.image = "default"

            if os.path.isfile("static/media/" + aux +"_ESPALDA.png") == True:
                p.secundaria = aux + "_ESPALDA.png"
            
            
            

            if (os.path.isfile("static/media/" + aux + "_FRENTE.png") == True) and not Images.objects.filter(image = aux + "_FRENTE.png"):
                Images.objects.create(product = Product.objects.get(id = p.id), image = aux + "_FRENTE.png")
            if (os.path.isfile("static/media/" + aux + "_ESPALDA.png") == True) and not Images.objects.filter(image = aux + "_ESPALDA.png"):
                Images.objects.create(product = Product.objects.get(id = p.id), image = aux + "_ESPALDA.png")    
            if (os.path.isfile("static/media/" + aux + "_DORSO.png") == True) and not Images.objects.filter(image = aux + "_DORSO.png"):
                Images.objects.create(product = Product.objects.get(id = p.id), image = aux + "_DORSO.png")
            
            
            
            p.save()
        
    



@admin.register(Talles)
class TallesAdmin(ImportExportModelAdmin):
    
    list_display = ('get_pk', 'subcodigo', 'get_name', 'id', 'product', 'talle', 'cantidad')
    
    def get_name(self, obj):
        return obj.product.name
    
    def get_pk(self, obj):
        return obj.product.pk
    


@admin.register(Images)
class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource
    pass

admin.site.register(Secciones, SeccionesAdmin)

#---------- admin actions



