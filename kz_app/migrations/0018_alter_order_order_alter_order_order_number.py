# Generated by Django 4.0.4 on 2022-05-06 09:40

from django.db import migrations, models
import kz_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0017_order_order_status_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=kz_app.models.random_num, max_length=5),
        ),
    ]
