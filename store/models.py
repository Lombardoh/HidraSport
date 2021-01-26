from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=20)
    destacada = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.nombre
    
class Importar(models.Model):
    codigo_de_barras = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    subcodigo = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    guard = models.CharField(max_length=50, blank=True, null=True)
    telas = models.CharField(max_length=50, blank=True, null=True)
    diseño = models.CharField(max_length=50, blank=True, null=True)
    detalle_color = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    secundaria = models.ImageField(upload_to='products/')
    price = models.FloatField()
    talle = models.CharField(max_length=20, blank=True, null=True)
    codigo_de_barras = models.CharField(max_length=100)
    largo = models.CharField(max_length=50, blank=True, null=True)
    cadera = models.CharField(max_length=50, blank=True, null=True)
    manga = models.CharField(max_length=50, blank=True, null=True)
    siza = models.CharField(max_length=50, blank=True, null=True)
    tiro = models.CharField(max_length=50, blank=True, null=True)
    bajo_busto = models.CharField(max_length=50, blank=True, null=True)
    cintura = models.CharField(max_length=50, blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    tamaño_caja = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default = 0, blank=True, null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Importar"
    
class Product(models.Model):
    codigo_de_barras= models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    subcodigo = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    guard = models.CharField(max_length=50, blank=True, null=True)
    telas = models.CharField(max_length=50, blank=True, null=True)
    diseño = models.CharField(max_length=50, blank=True, null=True)
    detalle_color = models.CharField(max_length=50, blank=True, null=True)
    faltante = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    secundaria = models.ImageField(upload_to='products/')
    categorias = models.ManyToManyField('Categorias', related_name='categorias', blank=True)
    price = models.FloatField()
    oferta = models.BooleanField(default=False)
    lomejor = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    proveedores = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Productos"
    
    
class Talles(models.Model):
    codigo_de_barras= models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    subcodigo = models.CharField(max_length=50)
    product = models.ForeignKey(Product, null = True, blank = True, on_delete=models.CASCADE)
    talle = models.CharField(max_length=20, blank=True, null=True)
    codigo_de_barras = models.CharField(max_length=100)
    largo = models.CharField(max_length=50, blank=True, null=True)
    cadera = models.CharField(max_length=50, blank=True, null=True)
    manga = models.CharField(max_length=50, blank=True, null=True)
    siza = models.CharField(max_length=50, blank=True, null=True)
    tiro = models.CharField(max_length=50, blank=True, null=True)
    bajo_busto = models.CharField(max_length=50, blank=True, null=True)
    cintura = models.CharField(max_length=50, blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    tamaño_caja = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default = 0, blank=True, null=True)
    
    def __str__(self):
        return self.talle
    class Meta:
        verbose_name_plural = "Talles"

    
class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/', help_text="La imagen debe ser 1.5 mas ancha que alta. Minimo 1000x670px ")
    categorias = models.OneToOneField('Categorias', related_name='secciones', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Secciones"
    
class Images(models.Model): #expense
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.product.name)
    
    class Meta:
        verbose_name_plural = "Imagenes"