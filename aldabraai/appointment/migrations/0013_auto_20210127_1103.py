# Generated by Django 3.0.5 on 2021-01-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0012_auto_20210127_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_state',
            field=models.CharField(choices=[('RE', 'Requested'), ('AC', 'Accepted'), ('DE', 'Declined')], default='RE', max_length=15),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(choices=[('DU', 'Due'), ('TK', 'Taken')], default='DU', max_length=5),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='booking_channel',
            field=models.CharField(choices=[('OP', 'App'), ('OC', 'Call')], default='OP', max_length=5),
        ),
    ]
