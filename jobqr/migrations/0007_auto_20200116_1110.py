# Generated by Django 2.2.9 on 2020-01-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobqr', '0006_jobimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobimage',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='jobs/'),
        ),
    ]
