from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField

User = get_user_model()


class ITAsset (models.Model):
    ''' Описание ИТ актива. '''
    title = models.CharField(
        max_length=255,
        verbose_name='Описание ИТ актива')
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
        verbose_name='Сервера/инстансы'
    )
    ipscope = RichTextField(
        verbose_name='Адресное пространство'
    )
    relations = RichTextField(
        verbose_name='Зависимости ПО и версии'
    )
    settings = RichTextField(
        verbose_name='Текущие настройки'
    )
    # Конец топологии.

    components = RichTextField(
        verbose_name='Компоненты системы'
    )
    management = RichTextField(
        verbose_name='Порядок управления'
    )
    access = RichTextField(
        verbose_name='Порядок доступа'
    )
    userlist = RichTextField(
        verbose_name='Учетные записи'
    )
    regulations = RichTextField(
        verbose_name='Регламентные действия'
    )
    additional_info = RichTextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )

    # Системное.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='itasset',
        verbose_name='Автор'
    )
    slug = models.SlugField(
        verbose_name='URL идентификатор',
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'ИТ Актив'
        verbose_name_plural = 'ИТ актив'
