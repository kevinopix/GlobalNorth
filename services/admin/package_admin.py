from django.contrib import admin
from services.models import Package
from services.resources import PackageResource
from import_export.admin import ImportExportModelAdmin
from .package_price_admin import PackagePriceAdmin


class PackageAdmin(ImportExportModelAdmin):
    model = Package
    resource_class = PackageResource
    list_display = ('name', 'is_active')
    inlines = (PackagePriceAdmin,)
    list_editable = ('is_active',)


admin.site.register(Package, PackageAdmin)