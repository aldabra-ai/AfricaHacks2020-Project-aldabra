# Generated by Django 3.0.5 on 2021-01-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=200, verbose_name='Users First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Users Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Users Date Of Birth')),
                ('username', models.CharField(max_length=300, unique=True, verbose_name='Users Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Users Email Address')),
                ('profile_type', models.CharField(choices=[('PT', 'Patient'), ('DR', 'Doctor')], max_length=10)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
