# Generated by Django 3.0.8 on 2020-07-24 13:37

import crmapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0012_auto_20200216_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='photo',
            field=models.ImageField(blank=True, upload_to=crmapp.models.get_timestamp_path, verbose_name='Фото'),
        ),
    ]
