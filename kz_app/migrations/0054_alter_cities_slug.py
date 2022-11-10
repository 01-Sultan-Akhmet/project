# Generated by Django 4.0.4 on 2022-05-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0053_cities_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='slug',
            field=models.SlugField(default='slug', max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]
