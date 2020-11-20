# Generated by Django 3.0.8 on 2020-11-20 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201120_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talles',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Talles'),
            preserve_default=False,
        ),
    ]
