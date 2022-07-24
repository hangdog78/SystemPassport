
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from .fields import SecureCharField

User = get_user_model()


class ITAssetGroup (models.Model):
    '''Типы активов. '''
    title = models.CharField(
        verbose_name='Наименование группы',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='URL идентификатор',
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )
    image = models.ImageField(
        'Баннер группы',
        upload_to='itasset/group',
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class ITAsset (models.Model):
    ''' Описание ИТ актива. '''
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование актива')
    description = models.TextField(
        verbose_name='Описание функционала',
        help_text='Описание основного функционала'
    )

    # Топология.
    allocation = RichTextField(
        verbose_name='Размещение',
        help_text='Информация о развертывании ассета'
    )
    instances = RichTextField(
        verbose_name='Сервера/инстансы',
        blank=True,
    )
    ipscope = RichTextField(
        verbose_name='Адресное пространство',
        blank=True,
    )
    relations = RichTextField(
        verbose_name='Зависимости ПО и версии',
        blank=True,
    )
    settings = RichTextField(
        verbose_name='Текущие настройки',
        blank=True,
    )
    # Конец топологии.

    components = RichTextField(
        verbose_name='Компоненты системы',
        blank=True,
    )
    management = RichTextField(
        verbose_name='Порядок управления',
        blank=True,
    )
    access = RichTextField(
        verbose_name='Порядок доступа',
        blank=True,
    )
    userlist = SecureCharField(
        verbose_name='Учетные записи',
        blank=True,
        max_length=1024,
    )
    regulations = RichTextField(
        verbose_name='Регламентные действия',
        blank=True,
    )
    additional_info = RichTextField(
        verbose_name='Дополнительная информация',
        blank=True,
    )

    # Системное.
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='itasset',
        verbose_name='Автор'
    )
    slug = models.SlugField(
        verbose_name='URL идентификатор',
        unique=True
    )
    image = models.ImageField(
        'Баннер актива',
        upload_to='itasset/assets/',
        blank=True
    )
    group = models.ForeignKey(
        ITAssetGroup,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='itasset',
        verbose_name='Группа активов',
        help_text='Группа, к которой будет относиться актив'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'ИТ Актив'
        verbose_name_plural = 'ИТ актив'
