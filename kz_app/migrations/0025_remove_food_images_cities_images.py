# Generated by Django 4.0.4 on 2022-05-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0024_remove_cities_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='images',
        ),
        migrations.AddField(
            model_name='cities',
            name='images',
            field=models.ImageField(blank=True, max_length=200, upload_to='static/'),
        ),
    ]