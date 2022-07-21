from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import ITAsset


class ITAssetForm(forms.ModelForm):
    title = forms.CharField(
        label="Наименование",
    )
    description = forms.CharField(
        label="Описание ассета",
    )
    allocation = forms.CharField(
        widget=CKEditorWidget(),
        label="Размещение ассета",
    )

    class Meta:
        model = ITAsset
        fields = ('title',
                  'description',
                  'allocation',
                  'image')
