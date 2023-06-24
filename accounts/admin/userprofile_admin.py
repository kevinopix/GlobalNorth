from django.contrib import admin
from accounts.models import UserProfile
from accounts.resources import UserProfileResource
from import_export.admin import ImportExportModelAdmin


class UserProfileAdmin(ImportExportModelAdmin):
    model = UserProfile
    resource_class = UserProfileResource
    list_display = ('user','location','terms_conditions_accepted')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)