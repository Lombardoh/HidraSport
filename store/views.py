from django.shortcuts import render, get_object_or_404
from store.models import Product, Categorias, Secciones, Images, Talles

from django.db.models import Count, Max

# def function name

def index(request):
    secciones = Secciones.objects.all()
    lomejor = Product.objects.filter(categorias__nombre__contains="lomejor")
    destacadas=Categorias.objects.filter(destacada=True)
    
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
    
    context = {
        "secciones": secciones,
        "lomejor": lomejor,
        "destacadas": destacadas
    }
    return render(request, 'index.html', context)

def filtro(request, categoria):
    articulos = Product.objects.filter( categorias__nombre__contains=categoria).order_by('name')
    destacadas=Categorias.objects.filter(destacada=True)
    banner=Categorias.objects.filter(nombre=categoria)
    context = {
        "categoria": categoria, 
        "articulos": articulos,
        "destacadas": destacadas,
        "banner": banner
    }
    return render(request, "filtro.html", context)

def filtro_images(request, pk):
    images = Images.objects.filter(product=pk)
    
    context = {
        'images':images
    }
    return (request, 'filtro.html', context)

def articulo_detalle(request, pk):
    articulo = Product.objects.get(pk=pk)
    images = Images.objects.filter(product=pk)
    destacadas=Categorias.objects.filter(destacada=True)
    context = {
        'articulo': articulo,
        "destacadas": destacadas,
        "images": images 
    }
    return render(request, 'articulo_detalle.html', context)
