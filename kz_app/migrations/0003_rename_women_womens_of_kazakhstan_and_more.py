# Generated by Django 4.0.2 on 2022-04-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz_app', '0002_category_women_cat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Women',
            new_name='Womens_of_Kazakhstan',
        ),
        migrations.AlterModelOptions(
            name='womens_of_kazakhstan',
            options={'verbose_name': ('Women_of_Kazakhstan',), 'verbose_name_plural': 'Womens_of_Kazakhstan'},
        ),
    ]
