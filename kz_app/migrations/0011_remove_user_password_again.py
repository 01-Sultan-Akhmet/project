# Generated by Django 4.0.2 on 2022-04-13 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0010_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_again',
        ),
    ]