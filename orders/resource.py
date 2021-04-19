from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export import fields, resources
from store.models import Order, ProductsInOrder

class ImagesResource(resources.ModelResource):

    class Meta:
        model = ProductsInOrder
        fields = ('product__name',)