from django.shortcuts import render, get_object_or_404
from store.models import Product, Categorias, Secciones, Images, Talles, Subcategorias, SubCatCol
from functools import reduce
from django.db.models import Count, Max, Q
import os
from django.http import HttpResponse, HttpResponseRedirect
# def function name

def index(request):
    secciones = Secciones.objects.all()
    lomejor = Product.objects.filter(categorias__nombre__contains="lomejor")
    destacadas=Categorias.objects.filter(destacada=True)
    subcategorias = Subcategorias.objects.all()
    subcatcol = SubCatCol.objects.all()
    
    context = {
        "secciones": secciones,
        "lomejor": lomejor,
        "destacadas": destacadas,
        "subcategorias": subcategorias
    }
    return render(request, 'index.html', context)

def filtro(request, product):
    
    aux = product.split('-')
    
    for x in aux:
        articulos = Product.objects.filter(categorias__nombre=x)
    print(aux)
    print(articulos)
    
    list_of_ids = []
    
    for x in articulos:
        if os.path.isfile("static/" + x.image.url):
            list_of_ids.append(x.id)
            
    articulos = Product.objects.filter(id__in=list_of_ids)
    print(list_of_ids)
    
    destacadas=Categorias.objects.filter(destacada=True)
    banner=Categorias.objects.filter(nombre=aux[0])
    context = {
        "product": product, 
        "articulos": articulos,
        "destacadas": destacadas,
        "banner": banner
    }
    return render(request, "filtro.html", context)

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

def product_list(request, name):

    prods = Product.objects.all()
    filter = []
    filter.append("all")

    for prod in prods:
        if prod.name not in filter:
            filter.append(prod.name)

    if name == "all":
        productos = Product.objects.all()
    else:
        productos = Product.objects.filter(name = name)
    
    destacadas=Categorias.objects.filter(destacada=True)
    context = {
        'productos': productos,
        "destacadas": destacadas,
        "filter": filter        
    }
    return render(request, 'product_list.html', context)

def file_upload_view(request, id):
    #print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        obj = Product.objects.get(id=id)
        Images.objects.create(product = obj, image=my_file)
    return HttpResponse('upload')

def file_delete_view(request, id):
    #print(request.FILES)
    obj = Images.objects.get(id = id)
    obj.delete()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

