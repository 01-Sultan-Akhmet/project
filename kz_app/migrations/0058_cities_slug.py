# Generated by Django 4.0.4 on 2022-05-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0057_remove_cities_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]