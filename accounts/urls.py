from django.urls import path, re_path
from accounts.views import UserRegisterView, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/register/', UserRegisterView.as_view(), name='register'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    # # path('accounts/new_inst_user/', AddInstUserView.as_view(), name='new_inst_user'),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"),
        name='password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
    #     name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
    #     name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
    #     name='password_reset_complete'),
]