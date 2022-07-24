from django.contrib import admin

from .models import ITAsset, ITAssetGroup


class ITAssetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
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
        'author',
        'slug',
    )
    list_filter = ('title', 'slug')
    empty_value_display = '-пусто-'


class ITAssetGroupAdmin (admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
    )

admin.site.register(ITAsset, ITAssetAdmin)
admin.site.register(ITAssetGroup, ITAssetGroupAdmin)