# Generated by Django 3.0.3 on 2020-02-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_kit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='redirect_to_form_with_query_params',
            field=models.BooleanField(default=False),
        ),
    ]
