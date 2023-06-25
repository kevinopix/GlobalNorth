from django.contrib import admin
from services.models import Service
from import_export.admin import ImportExportModelAdmin
from .serviceitem_admin import ServiceItemAdmin


class ServiceAdmin(ImportExportModelAdmin):
    model = Service
    list_display = ('name', 'is_active')
    inlines = (ServiceItemAdmin,)
    list_editable = ('is_active',)


admin.site.register(Service, ServiceAdmin)