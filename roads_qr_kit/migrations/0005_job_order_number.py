# Generated by Django 3.0.5 on 2020-06-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads_qr_kit', '0004_jobimage_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='order_number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
