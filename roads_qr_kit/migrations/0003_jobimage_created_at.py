# Generated by Django 3.0.3 on 2020-04-30 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roads_qr_kit', '0002_auto_20200429_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]