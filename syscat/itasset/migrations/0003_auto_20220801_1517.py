# Generated by Django 3.2.14 on 2022-08-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itasset', '0002_itassetfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itassetfile',
            options={'ordering': ('asset_file',), 'verbose_name': 'Файл приложение', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterField(
            model_name='itassetfile',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание файла'),
        ),
    ]