# Generated by Django 3.0.5 on 2021-01-18 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0002_auto_20210118_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospitaldb.Block'),
        ),
    ]
