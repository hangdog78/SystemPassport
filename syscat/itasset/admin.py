from django.contrib import admin

from .models import SysTopology


class TopologyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'allocation'
    )

admin.site.register(SysTopology, TopologyAdmin)
