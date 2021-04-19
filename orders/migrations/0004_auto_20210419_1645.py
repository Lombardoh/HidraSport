# Generated by Django 3.0.8 on 2021-04-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210419_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsinorder',
            old_name='produc',
            new_name='product',
        ),
        migrations.AddField(
            model_name='productsinorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Order'),
        ),
    ]
