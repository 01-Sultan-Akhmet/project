# Generated by Django 4.0.4 on 2022-05-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0050_alter_university_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='location',
            field=models.CharField(max_length=250),
        ),
    ]
