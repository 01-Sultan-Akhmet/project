# Generated by Django 4.0.4 on 2022-05-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0013_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('place', models.CharField(default='eat_here', max_length=50)),
                ('order', models.CharField(max_length=250)),
                ('total', models.IntegerField(unique=True)),
                ('payment', models.CharField(default='card', max_length=50)),
                ('time', models.TimeField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
