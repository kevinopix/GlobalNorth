from django.contrib import admin
from termsandconditions.models import Terms
from import_export.admin import ImportExportModelAdmin

class TermsAdmin(ImportExportModelAdmin):
    model = Terms
    list_display = ('terms_and_conditions','is_active')
    list_editable = ('is_active',)


admin.site.register(Terms, TermsAdmin)