from django.urls import path, re_path
from services.views import PackageViewerView


urlpatterns = [
    path('services/package/<int:pk>/view/', PackageViewerView.as_view(), name="view_package"),
]