# Generated by Django 3.0.5 on 2021-01-18 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldb', '0002_auto_20210118_2000'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210118_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientBankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=500)),
                ('account_name', models.CharField(max_length=350)),
                ('account_number', models.CharField(max_length=11)),
                ('branch_name', models.CharField(max_length=300)),
                ('branch_code', models.CharField(max_length=6)),
                ('swift_code', models.CharField(max_length=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='doctorspecialization',
            old_name='Specialization',
            new_name='specialization',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='hospital',
        ),
        migrations.AddField(
            model_name='doctor',
            name='residing_hospital',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='hospitaldb.Hospital'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PatientReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_name', models.CharField(max_length=500, verbose_name='The review name or summary')),
                ('is_review_anonymous', models.BooleanField(default=False)),
                ('wait_time_rating', models.FloatField(blank=True, max_length=3)),
                ('bedside_manner_rating', models.FloatField(blank=True, max_length=3)),
                ('overall_rating', models.FloatField(max_length=5)),
                ('review', models.TextField(blank=True, max_length=4000)),
                ('is_doctor_recommended', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=('Y', 'Yes'), max_length=1)),
                ('not_recommended_reason', models.TextField(max_length=2000, verbose_name='A Reason for not recommending this Doctor')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reviewed_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Doctor')),
            ],
            options={
                'ordering': ['review_name'],
            },
        ),
        migrations.CreateModel(
            name='PatientInsurranceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurrance_company', models.CharField(max_length=500)),
                ('insurrance_name', models.CharField(max_length=300)),
                ('insurrance_account_name', models.CharField(max_length=300)),
                ('insurrance_account_no', models.CharField(max_length=12)),
                ('bank_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.PatientBankDetail')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AffiliatedHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('affiliation_relationship', models.CharField(help_text='What relationship do have with the hospital, what do you do there', max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('affiliated_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
