# Generated by Django 3.0.8 on 2021-04-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210428_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='secundaria',
            field=models.ImageField(default=0, upload_to='products/'),
            preserve_default=False,
        ),
    ]