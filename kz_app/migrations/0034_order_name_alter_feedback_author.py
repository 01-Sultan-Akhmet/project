# Generated by Django 4.0.4 on 2022-05-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0033_alter_cities_image_alter_food_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]