from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=20)
    destacada = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return '{}'.format(self.nombre)

class Product(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    portada = models.ImageField(upload_to='products/')
    secundaria = models.ImageField(upload_to='products/')
    categorias = models.ManyToManyField('Categorias', related_name='categorias')
    price = models.FloatField()
    cantidad = models.IntegerField(default=0)
    oferta = models.BooleanField(default=False)
    LoMejor = models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.name)
    
class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/')
    categorias = models.OneToOneField('Categorias', related_name='secciones', on_delete=models.CASCADE)
    
class Images(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.product.name)