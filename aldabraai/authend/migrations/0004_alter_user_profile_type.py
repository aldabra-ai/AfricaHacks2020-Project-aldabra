# Generated by Django 3.2 on 2021-05-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authend', '0003_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_type',
            field=models.CharField(choices=[('PT', 'Patient'), ('DR', 'Doctor')], max_length=10),
        ),
    ]