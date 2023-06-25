from django.contrib import admin
from services.models import ServiceItem


class ServiceItemAdmin(admin.StackedInline):
    model = ServiceItem