# Generated by Django 4.0.4 on 2022-05-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0015_remove_order_payment_remove_order_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='83722', max_length=5),
        ),
    ]
