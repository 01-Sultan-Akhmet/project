# Generated by Django 4.0.4 on 2022-05-22 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0046_south_id_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='south',
            name='id_num',
        ),
    ]