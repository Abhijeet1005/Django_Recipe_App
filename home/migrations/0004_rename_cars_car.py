# Generated by Django 4.2.3 on 2023-08-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cars'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]