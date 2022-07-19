from django.db import models
from django_editorjs import EditorJsField


class SysTopology(models.Model):
    ''' Топология системы. '''
    title = models.CharField(
        max_length=255,
        verbose_name='Описание топологии')
    allocation = EditorJsField(
        verbose_name='Размещение'
    )

    def __str__(self):
        return self.title
