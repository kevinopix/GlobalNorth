from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from accounts.forms import UserCreationForm, UserChangeForm
from accounts.models import User
from accounts.resources import UserResorce
from import_export.admin import ImportExportModelAdmin


class UserAdmin(ImportExportModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    resource_class = UserResorce
    list_display = ('email','first_name','last_name', 'is_staff', 'is_active','profile_pk_value')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name','last_name','password')}),
        ('Permissions', {'fields': ('is_staff','is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2', 'is_staff','is_superuser', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)