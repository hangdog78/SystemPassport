from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth import get_user_model

from .models import ITAsset

User = get_user_model()


class ITAssetForm(forms.ModelForm):
    ''' Форма создания актива. '''
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
    files = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        ),
        label="Файлы",
        required=False,
        help_text="Конфигурационные файлы и т.д."
    )
    secured_users = forms.ModelMultipleChoiceField(
        label="Доверенные пользователи",
        queryset=User.objects.all().order_by("username"),
        required=False,
        help_text="Укажите пользователей, имеющих доступ к защищенным разделам"
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
            'additional_info',
            'files',
            'secured_users'
        )
