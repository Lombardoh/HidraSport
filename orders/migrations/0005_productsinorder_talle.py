# Generated by Django 3.0.8 on 2021-05-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210419_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsinorder',
            name='talle',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
