from django.contrib import admin
from services.models import Package
from services.resources import PackageResource
from import_export.admin import ImportExportModelAdmin


class PackageAdmin(ImportExportModelAdmin):
    model = Package
    resource_class = PackageResource
    list_display = ('name', 'price', 'is_active')


admin.site.register(Package, PackageAdmin)