# Generated by Django 3.0.3 on 2020-02-16 15:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200216_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]
