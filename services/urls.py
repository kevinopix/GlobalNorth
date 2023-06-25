from django.urls import path, re_path
from services.views import *


urlpatterns = [
    path('services/package/<int:pk>/view/', PackageViewerView.as_view(), name="view_package"),
    path('services/package/list', PackagesListView.as_view(), name="list_packages"),
    path('services/service/<int:pk>/view/', ServiceViewerView.as_view(), name="view_package"),
    path('services/service/list', ServicesListView.as_view(), name="list_services"),
]