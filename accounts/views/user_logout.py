from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.conf import settings
from django.middleware.csrf import rotate_token

def logout_view(request):
    title = 'Logout'
    context = dict()
    context['project'] = settings.PROJECT_TITLE
    context['title'] = title
    logout(request)
    rotate_token(request)
    return render(request, "accounts/logout_form.html", context)