# Generated by Django 3.0.5 on 2021-02-27 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210226_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinsurrancedetail',
            name='bank_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='account.PatientBankDetail'),
        ),
    ]