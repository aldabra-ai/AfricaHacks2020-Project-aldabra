# Generated by Django 3.0.5 on 2021-01-21 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0006_auto_20210119_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctoroffice',
            old_name='office_owner',
            new_name='officeowner',
        ),
    ]