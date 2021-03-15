# Generated by Django 3.0.8 on 2021-03-15 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_subcategorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorias',
            name='categoria',
        ),
        migrations.CreateModel(
            name='SubCatCol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('destacada', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Categorias')),
            ],
        ),
        migrations.AddField(
            model_name='subcategorias',
            name='subcatcol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.SubCatCol'),
            preserve_default=False,
        ),
    ]
