# Generated by Django 5.0.6 on 2024-06-06 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_alter_doctor_available_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon')], max_length=50)),
                ('speciality', models.CharField(choices=[('OB/GYN', 'OB/GYN'), ('Pediatrician', 'Pediatrician'), ('Dermatologist', 'Dermatologist'), ('Cardiologist', 'Cardiologist'), ('Orthopedist', 'Orthopedist')], max_length=100)),
                ('position', models.CharField(choices=[('Senior Consultant', 'Senior Consultant'), ('Registrar', 'Registrar'), ('Resident', 'Resident'), ('Intern', 'Intern')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctors'),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
