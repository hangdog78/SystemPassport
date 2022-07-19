from django.contrib import admin

from .models import SysTopology


class TopologyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body'
    )

admin.site.register(SysTopology, TopologyAdmin)
