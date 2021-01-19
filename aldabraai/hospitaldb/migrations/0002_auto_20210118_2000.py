# Generated by Django 3.0.5 on 2021-01-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='block_name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
        migrations.AddField(
            model_name='hospital',
            name='slug',
            field=models.SlugField(default='hospital_name', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_type',
            field=models.CharField(choices=[('SC', 'Special Clinic'), ('TH', 'Tranditional Hospital')], default=('TH', 'Tranditional Hospital'), max_length=30),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='rank',
            field=models.FloatField(max_length=5),
        ),
    ]
