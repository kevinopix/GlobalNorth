from django.contrib import admin
from services.models import Price
# from services.resources import PackagePriceResource
# from import_export.admin import ImportExportModelAdmin


class PackagePriceAdmin(admin.StackedInline):
    model = Price
    # resource_class = PackagePriceResource
    # list_display = ('product', 'price')


# admin.site.register(Price, PackagePriceAdmin)