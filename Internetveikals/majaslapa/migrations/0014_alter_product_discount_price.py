# Generated by Django 4.1.2 on 2023-01-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0013_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, error_messages={'name': {'max_lenght': 'Cenai jābūt no 0 līdz 9999,99!'}}, help_text='Maksimalais ir 9999.99', max_digits=6, null=True, verbose_name='Atlaides cena'),
        ),
    ]
