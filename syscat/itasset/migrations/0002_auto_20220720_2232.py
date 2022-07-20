# Generated by Django 3.2.14 on 2022-07-20 18:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itasset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itasset',
            name='allocation',
            field=ckeditor.fields.RichTextField(help_text='Информация о развертывании ассета', verbose_name='Размещение'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='description',
            field=models.TextField(help_text='Описание основного функционала', verbose_name='Описание функционала'),
        ),
    ]
