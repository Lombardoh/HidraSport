# Generated by Django 3.0.8 on 2021-05-29 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210529_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importar',
            name='codigo_de_barras',
        ),
    ]
