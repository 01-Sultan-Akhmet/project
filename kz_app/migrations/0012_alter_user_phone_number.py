# Generated by Django 4.0.2 on 2022-04-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0011_remove_user_password_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='+7 ', max_length=15),
        ),
    ]
