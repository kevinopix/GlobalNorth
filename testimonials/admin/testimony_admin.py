from django.contrib import admin
from testimonials.models import Testimony
from import_export.admin import ImportExportModelAdmin

class TestimonyAdmin(ImportExportModelAdmin):
    model = Testimony
    list_display = ('testimony_by','is_active')
    list_editable = ('is_active',)


admin.site.register(Testimony, TestimonyAdmin)