from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import ITAsset


class ITAssetForm(forms.ModelForm):
    allocation = forms.CharField(
        widget=CKEditorWidget(),
        label="Размещение актива",
    )
    instances = forms.CharField(
        widget=CKEditorWidget(),
        label="Сервера/инстансы",
        required=False
    )
    ipscope = forms.CharField(
        widget=CKEditorWidget(),
        label="Адресное пространство"
    )
    relations = forms.CharField(
        widget=CKEditorWidget(),
        label="Зависимости ПО и версии",
        required=False
    )
    settings = forms.CharField(
        widget=CKEditorWidget(),
        label="Текущие настройки",
        required=False
    )
    components = forms.CharField(
        widget=CKEditorWidget(),
        label="Компоненты системы",
        required=False
    )
    management = forms.CharField(
        widget=CKEditorWidget(),
        label="Порядок управления",
        required=False
    )
    access = forms.CharField(
        widget=CKEditorWidget(),
        label="Порядок доступа",
        required=False
    )
    userlist = forms.CharField(
        widget=CKEditorWidget(),
        label="Учетные записи",
        required=False
    )
    regulations = forms.CharField(
        widget=CKEditorWidget(),
        label="Регламентные действия",
        required=False
    )
    additional_info = forms.CharField(
        widget=CKEditorWidget(),
        label="Дополнительная информация",
        required=False
    )

    class Meta:
        model = ITAsset
        fields = (
            'image',
            'group',
            'title',
            'description',
            'allocation',
            'instances',
            'ipscope',
            'relations',
            'settings',
            'components',
            'management',
            'access',
            'userlist',
            'regulations',
            'additional_info'
            )
