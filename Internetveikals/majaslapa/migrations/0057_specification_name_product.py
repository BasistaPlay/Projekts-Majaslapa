# Generated by Django 4.1.2 on 2022-12-27 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0056_remove_specification_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification_name',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='majaslapa.product'),
        ),
    ]