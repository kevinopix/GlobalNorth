from django.contrib import admin
from home.models import Vision
from home.resources import VisionResource
from import_export.admin import ImportExportModelAdmin


class VisionAdmin(ImportExportModelAdmin):
    model = Vision
    resource_class = VisionResource
    list_display = ('vision_text', 'is_active')


admin.site.register(Vision, VisionAdmin)