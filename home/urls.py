from django.urls import path, re_path
from home.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]