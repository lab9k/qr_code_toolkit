# Generated by Django 3.0.3 on 2020-02-11 16:08

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrackedItem',
            fields=[
                ('item_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('is_in_use', models.BooleanField(default=False)),
                ('missing', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_items', to='qr_kit.Job')),
            ],
        ),
        migrations.CreateModel(
            name='JobImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img/jobs/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='qr_kit.Job')),
            ],
        ),
    ]
