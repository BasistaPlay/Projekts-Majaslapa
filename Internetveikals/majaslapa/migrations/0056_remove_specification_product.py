# Generated by Django 4.1.2 on 2022-12-27 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0055_alter_specification_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='product',
        ),
    ]