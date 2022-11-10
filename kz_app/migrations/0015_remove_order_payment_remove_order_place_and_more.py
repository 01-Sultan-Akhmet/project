# Generated by Django 4.0.4 on 2022-05-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0014_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='18858', max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(),
        ),
    ]
