# Generated by Django 3.0.8 on 2020-11-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201113_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Descripción',
            new_name='descripción',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='LoMejor',
            new_name='lomejor',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Sexo',
            new_name='sexo',
        ),
        migrations.AddField(
            model_name='categorias',
            name='product',
            field=models.ManyToManyField(related_name='product', to='store.Product'),
        ),
    ]
