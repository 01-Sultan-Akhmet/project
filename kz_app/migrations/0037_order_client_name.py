# Generated by Django 4.0.4 on 2022-05-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0036_remove_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_name',
            field=models.CharField(default='Sultan', max_length=100),
        ),
    ]
