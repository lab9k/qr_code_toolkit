# Generated by Django 2.2.4 on 2019-11-06 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobqr', '0002_auto_20191014_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackeditem',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_items', to='jobqr.Job'),
        ),
    ]
