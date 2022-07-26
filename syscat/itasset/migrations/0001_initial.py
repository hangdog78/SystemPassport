# Generated by Django 3.2.14 on 2022-07-25 06:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import itasset.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ITAssetGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование группы')),
                ('slug', models.SlugField(unique=True, verbose_name='URL идентификатор')),
                ('description', models.TextField(verbose_name='Описание группы')),
                ('image', models.ImageField(blank=True, upload_to='itasset/group', verbose_name='Баннер группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ITAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование актива')),
                ('description', models.TextField(help_text='Описание основного функционала', verbose_name='Описание функционала')),
                ('allocation', ckeditor.fields.RichTextField(help_text='Информация о развертывании ассета', verbose_name='Размещение')),
                ('instances', ckeditor.fields.RichTextField(blank=True, verbose_name='Сервера/инстансы')),
                ('ipscope', ckeditor.fields.RichTextField(blank=True, verbose_name='Адресное пространство')),
                ('relations', ckeditor.fields.RichTextField(blank=True, verbose_name='Зависимости ПО и версии')),
                ('settings', ckeditor.fields.RichTextField(blank=True, verbose_name='Текущие настройки')),
                ('components', ckeditor.fields.RichTextField(blank=True, verbose_name='Компоненты системы')),
                ('management', ckeditor.fields.RichTextField(blank=True, verbose_name='Порядок управления')),
                ('access', ckeditor.fields.RichTextField(blank=True, verbose_name='Порядок доступа')),
                ('userlist', itasset.fields.SecureCharField(blank=True, max_length=1024, verbose_name='Учетные записи')),
                ('regulations', ckeditor.fields.RichTextField(blank=True, verbose_name='Регламентные действия')),
                ('additional_info', ckeditor.fields.RichTextField(blank=True, verbose_name='Дополнительная информация')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('slug', models.SlugField(unique=True, verbose_name='URL идентификатор')),
                ('image', models.ImageField(blank=True, upload_to='itasset/assets/', verbose_name='Баннер актива')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itasset', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('group', models.ForeignKey(blank=True, help_text='Группа, к которой будет относиться актив', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itasset', to='itasset.itassetgroup', verbose_name='Группа активов')),
            ],
            options={
                'verbose_name': 'ИТ Актив',
                'verbose_name_plural': 'ИТ актив',
                'ordering': ('-created',),
            },
        ),
    ]
