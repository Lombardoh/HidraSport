# Generated by Django 3.0.8 on 2021-05-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210529_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importar',
            name='bajo_busto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='cadera',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='cintura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='largo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='manga',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='siza',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='talle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='importar',
            name='tiro',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
