from django.db import models
from django_editorjs import EditorJsField


class SysTopology
    ''' Топология системы. '''
    title = models.CharField(
        max_length=255,
        verbose_name = 'Описание топологии')
    body = EditorJsField()

    def __str__(self):
        return self.title
    
