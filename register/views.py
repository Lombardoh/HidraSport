from django.shortcuts import render, redirect
from .forms import CreateUserForm
from store.models import Product, Categorias, Secciones, Images
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    destacadas=Categorias.objects.filter(destacada=True)

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect("index")
    else:
        form = CreateUserForm()
        
    context = {
        "form":form,
        'destacadas':destacadas}
    return render(request, 'register/register.html', context)


    