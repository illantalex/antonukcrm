# Generated by Django 3.2.9 on 2021-12-11 09:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200724_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, upload_to=main.models.get_timestamp_path, verbose_name='Галерея'),
        ),
    ]