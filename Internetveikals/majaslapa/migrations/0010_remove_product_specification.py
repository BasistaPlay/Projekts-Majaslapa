# Generated by Django 4.1.2 on 2023-01-05 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0009_alter_product_specification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
    ]
