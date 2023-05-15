from django.urls import path, re_path
from home.views import HomeView, HomePageView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home', HomePageView.as_view(), name="home2")
]