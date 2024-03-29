# Generated by Django 3.2 on 2021-05-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authend', '0008_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_type',
            field=models.CharField(choices=[('PT', 'Patient'), ('DR', 'Doctor')], max_length=10, verbose_name='Register as'),
        ),
    ]
