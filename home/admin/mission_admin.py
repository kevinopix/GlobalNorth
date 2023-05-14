from django.contrib import admin
from home.models import Mission
from home.resources import MissionResource
from import_export.admin import ImportExportModelAdmin


class MissionAdmin(ImportExportModelAdmin):
    model = Mission
    resource_class = MissionResource
    list_display = ('mission_text', 'is_active')


admin.site.register(Mission, MissionAdmin)