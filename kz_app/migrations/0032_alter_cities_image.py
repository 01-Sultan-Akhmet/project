# Generated by Django 4.0.4 on 2022-05-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0031_alter_cities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='image',
            field=models.ImageField(default=True, upload_to='img/'),
        ),
    ]
