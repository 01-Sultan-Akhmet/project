# Generated by Django 4.0.4 on 2022-05-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0041_alter_cities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='img/%y'),
        ),
    ]
