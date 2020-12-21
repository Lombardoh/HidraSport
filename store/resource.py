from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export import fields, resources
from store.models import Product, Categorias, Secciones, Images, Talles


class ImagesResource(resources.ModelResource):

    class Meta:
        model = Images
        fields = ('image', 'product__name')

class TallesResource(resources.ModelResource):
    product_id = fields.Field(widget=ForeignKeyWidget(Product, 'pk'))
    class Meta:
        model = Talles
        fields = ('product_id',)