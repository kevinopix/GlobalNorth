from django.shortcuts import render
from django.contrib.auth import authenticate, logout


def logout_view(request):
    title = 'Logout'
    logout(request)
    return render(request, "accounts/logout_form.html", {'title': title})