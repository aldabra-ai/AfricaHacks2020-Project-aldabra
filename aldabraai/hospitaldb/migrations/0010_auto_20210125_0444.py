# Generated by Django 3.0.5 on 2021-01-25 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0009_auto_20210121_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officeschedule',
            old_name='days_available',
            new_name='day_available',
        ),
    ]