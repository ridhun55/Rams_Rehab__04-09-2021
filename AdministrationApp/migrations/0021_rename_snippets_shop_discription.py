# Generated by Django 3.2 on 2021-09-09 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrationApp', '0020_countervalues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='snippets',
            new_name='discription',
        ),
    ]