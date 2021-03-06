# Generated by Django 3.0.2 on 2020-02-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_manager_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Менеджер', 'verbose_name_plural': 'Менеджеры'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название'),
        ),
    ]
