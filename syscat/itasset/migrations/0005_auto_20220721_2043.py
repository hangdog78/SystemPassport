# Generated by Django 3.2.14 on 2022-07-21 16:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itasset', '0004_auto_20220721_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itasset',
            name='access',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Порядок доступа'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='additional_info',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='components',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Компоненты системы'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='instances',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Сервера/инстансы'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='ipscope',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Адресное пространство'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='management',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Порядок управления'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='regulations',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Регламентные действия'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='relations',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Зависимости ПО и версии'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='settings',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текущие настройки'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='userlist',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Учетные записи'),
        ),
    ]
