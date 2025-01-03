# Generated by Django 5.0.6 on 2024-05-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='available_from',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='available_to',
            field=models.TimeField(default='17:00'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
