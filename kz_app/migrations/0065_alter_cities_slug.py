# Generated by Django 4.0.4 on 2022-05-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0064_alter_cities_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='slug',
            field=models.SlugField(default=True, max_length=100, null=True, verbose_name='URL'),
        ),
    ]
