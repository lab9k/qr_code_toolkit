# Generated by Django 3.0.3 on 2020-06-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads_qr_kit', '0007_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(editable=False, max_length=128),
        ),
    ]
