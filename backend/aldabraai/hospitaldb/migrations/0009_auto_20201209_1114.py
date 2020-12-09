# Generated by Django 3.1.4 on 2020-12-09 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0008_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospitaldb.hospital'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
