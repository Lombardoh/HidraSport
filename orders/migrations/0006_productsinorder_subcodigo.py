# Generated by Django 3.0.8 on 2021-05-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productsinorder_talle'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsinorder',
            name='subcodigo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
