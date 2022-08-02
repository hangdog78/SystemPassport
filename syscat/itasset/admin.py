from django.contrib import admin

from .models import ITAsset, ITAssetGroup, ITAssetFile


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


class ITAssetFileAdmin (admin.ModelAdmin):
    list_display = (
        'pk',
        'asset_file',
        'asset',
    )

admin.site.register(ITAsset, ITAssetAdmin)
admin.site.register(ITAssetGroup, ITAssetGroupAdmin)
admin.site.register(ITAssetFile, ITAssetFileAdmin)