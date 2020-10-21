from django.shortcuts import render, redirect
from .forms import RegisterForm
from store.models import Product, Categorias, Secciones, Images

# Create your views here.
def register(response):
    destacadas=Categorias.objects.filter(destacada=True)
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("http://127.0.0.1:8000/")
    else:
        form = RegisterForm()
        
    context = {
        "form":form,
        'destacadas':destacadas}
    return render(response, 'register/register.html', context)