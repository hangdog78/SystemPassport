from django.contrib.auth import get_user_model
from django.db import models
from django_editorjs import EditorJsField

User = get_user_model()

class ITAsset (models.Model):
    ''' Описание ИТ актива. '''
    title = models.CharField(
        max_length=255,
        verbose_name='Описание ИТ актива')
    description = models.TextField(
        verbose_name='Описание функционала'
    )

    # Топология.
    allocation = EditorJsField(
        verbose_name='Размещение'
    )
    instances = EditorJsField(
        verbose_name='Сервера/инстансы'
    )
    ipscope = EditorJsField(
        verbose_name='Адресное пространство'
    )
    relations = EditorJsField(
        verbose_name='Зависимости ПО и версии'
    )
    settings = EditorJsField(
        verbose_name='Текущие настройки'
    )
    # Конец топологии.
    
    components = EditorJsField(
        verbose_name='Компоненты системы'
    )
    management = EditorJsField(
        verbose_name='Порядок управления'
    )
    access = EditorJsField(
        verbose_name='Порядок доступа'
    )
    userlist = EditorJsField(
        verbose_name='Учетные записи'
    )
    regulations = EditorJsField(
        verbose_name='Регламентные действия'
    )
    additional_info = EditorJsField(
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
