# Generated by Django 3.0.8 on 2021-05-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_productsinorder_subcodigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='totalPrice',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='direccionEntrega',
            field=models.TextField(blank=True, default=1, max_length=70),
            preserve_default=False,
        ),
    ]