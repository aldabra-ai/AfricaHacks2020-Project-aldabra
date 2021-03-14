# Generated by Django 3.0.5 on 2021-01-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_auto_20210127_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_state',
            field=models.CharField(choices=[('RE', 'Requested'), ('AC', 'Accepted'), ('DE', 'Declined')], default=('RE', 'Requested'), max_length=15),
        ),
    ]