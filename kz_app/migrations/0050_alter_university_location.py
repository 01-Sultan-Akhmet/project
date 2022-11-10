# Generated by Django 4.0.4 on 2022-05-22 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0049_alter_university_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='location',
            field=models.ForeignKey(default='Almaty', on_delete=django.db.models.deletion.CASCADE, to='kz_app.cities', verbose_name='Data'),
        ),
    ]
