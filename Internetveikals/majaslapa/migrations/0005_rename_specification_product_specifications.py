# Generated by Django 4.1.2 on 2023-01-05 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0004_alter_product_specification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='specification',
            new_name='specifications',
        ),
    ]