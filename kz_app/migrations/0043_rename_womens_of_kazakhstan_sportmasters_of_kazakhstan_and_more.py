# Generated by Django 4.0.4 on 2022-05-18 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0042_alter_cities_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Womens_of_Kazakhstan',
            new_name='Sportmasters_of_Kazakhstan',
        ),
        migrations.AlterModelOptions(
            name='sportmasters_of_kazakhstan',
            options={'verbose_name': ('Sportmasters_of_Kazakhstan',), 'verbose_name_plural': 'Sportmasters_of_Kazakhstan'},
        ),
    ]
