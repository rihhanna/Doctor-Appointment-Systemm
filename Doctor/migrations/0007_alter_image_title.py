# Generated by Django 5.0.6 on 2024-06-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(choices=[('MRI Scan', 'MRI Scan'), ('CT Scan', 'CT Scan'), ('MRA Scan', 'MRA Scan'), ('PET Scan', 'PET Scan'), ('X-ray Scan', 'X-ray Scan')], max_length=100),
        ),
    ]
