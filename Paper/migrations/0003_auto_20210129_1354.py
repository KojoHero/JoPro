# Generated by Django 3.1.5 on 2021-01-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paper', '0002_auto_20210129_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listmodel',
            old_name='expected_EndDate',
            new_name='endDate',
        ),
    ]
