# Generated by Django 4.1.2 on 2023-01-16 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0016_productspecification_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='majaslapa.producttype', verbose_name='Produkta Veids'),
        ),
    ]
