# Generated by Django 3.1.4 on 2020-12-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0009_auto_20201209_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Specialities'},
        ),
        migrations.AlterField(
            model_name='hospital',
            name='rank',
            field=models.CharField(choices=[('ONE', 1), ('TWO', 2), ('THREE', 3), ('FOUR', 4), ('FIVE', 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='treatment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]