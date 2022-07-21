# Generated by Django 3.2.14 on 2022-07-21 10:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itasset', '0003_itasset_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itasset',
            name='access',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Порядок доступа'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='components',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Компоненты системы'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='image',
            field=models.ImageField(blank=True, upload_to='itasset/', verbose_name='Баннер актива'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='instances',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Сервера/инстансы'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='ipscope',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Адресное пространство'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='management',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Порядок управления'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='regulations',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Регламентные действия'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='relations',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Зависимости ПО и версии'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='settings',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текущие настройки'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='userlist',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Учетные записи'),
        ),
    ]
