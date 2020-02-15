# Generated by Django 3.0.2 on 2020-02-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0009_auto_20200210_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': 'Ключевое слово', 'verbose_name_plural': 'Ключевые слова'},
        ),
        migrations.AlterField(
            model_name='message',
            name='kwords',
            field=models.ManyToManyField(blank=True, to='crmapp.Keyword', verbose_name='Ключевые слова'),
        ),
    ]
