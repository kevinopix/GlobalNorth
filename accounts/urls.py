from django.urls import path, re_path
from accounts.views import \
    UserRegisterView, PasswordResetRequestView, UserProfileRegisterView, \
    UserLoginView, UserLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/register/', UserRegisterView.as_view(), name='register'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', PasswordResetRequestView.as_view(), name='password_request'),
    re_path(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"),
        name='password_reset_done'),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"),
        name='password_reset_confirm'),
    re_path(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"),
        name='password_reset_complete'),
    path('accounts/profile/new/', UserProfileRegisterView.as_view(), name="new_user_profile"),
]