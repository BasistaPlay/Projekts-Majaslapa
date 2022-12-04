# Generated by Django 4.1.2 on 2022-12-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majaslapa', '0036_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='details',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='none', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='none', max_length=200),
        ),
    ]