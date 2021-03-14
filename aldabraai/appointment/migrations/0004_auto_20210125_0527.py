# Generated by Django 3.0.5 on 2021-01-25 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0010_auto_20210125_0444'),
        ('appointment', '0003_auto_20210121_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='booked_doctor_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospitaldb.DoctorOffice'),
        ),
    ]