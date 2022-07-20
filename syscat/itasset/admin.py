from django.contrib import admin

from .models import ITAsset


class ITAssetAdmin(admin.ModelAdmin):
    list_display =  (
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
    

admin.site.register(ITAsset, ITAssetAdmin)
