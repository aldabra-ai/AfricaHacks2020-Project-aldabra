# Generated by Django 3.1.7 on 2021-04-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0013_auto_20210402_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeschedule',
            name='day_available',
            field=models.DateField(unique=True),
        ),
    ]
