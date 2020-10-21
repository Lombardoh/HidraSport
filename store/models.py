from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=20)
    destacada = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return '{}'.format(self.nombre)

class Product(models.Model):
    name = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)
    largo = models.CharField(max_length=50)
    cadera = models.CharField(max_length=50)
    tiro = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    secundaria = models.ImageField(upload_to='products/')
    categorias = models.ManyToManyField('Categorias', related_name='categorias')
    price = models.FloatField()
    oferta = models.BooleanField(default=False)
    LoMejor = models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.name)
    
class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/', help_text="La imagen debe ser 1.5 mas ancha que alta. Minimo 1000x670px ")
    categorias = models.OneToOneField('Categorias', related_name='secciones', on_delete=models.CASCADE)
    
class Images(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.product.name)