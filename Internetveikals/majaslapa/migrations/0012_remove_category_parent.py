# Generated by Django 4.1.2 on 2023-01-05 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0011_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]