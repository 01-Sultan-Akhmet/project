# Generated by Django 4.0.4 on 2022-05-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0043_rename_womens_of_kazakhstan_sportmasters_of_kazakhstan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='city_id',
            field=models.IntegerField(default=1),
        ),
    ]
