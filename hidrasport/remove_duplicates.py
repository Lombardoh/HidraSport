from django.db.models import Count, Max

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