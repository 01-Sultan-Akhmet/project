# Generated by Django 4.0.4 on 2022-05-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0067_university_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='city_slug',
        ),
    ]