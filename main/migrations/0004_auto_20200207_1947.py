# Generated by Django 3.0.2 on 2020-02-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200206_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Фото'),
        ),
    ]
