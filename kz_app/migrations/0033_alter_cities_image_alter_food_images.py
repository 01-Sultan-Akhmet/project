# Generated by Django 4.0.4 on 2022-05-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0032_alter_cities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='image',
            field=models.ImageField(default=True, upload_to='static/kz_app/img/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='images',
            field=models.ImageField(default=True, upload_to='static/kz_app/img'),
        ),
    ]
