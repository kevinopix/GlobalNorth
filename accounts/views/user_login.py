from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.middleware.csrf import rotate_token


def login_view(request):
    rotate_token(request)
    title = "Login"
    form = UserLoginForm()
    context = dict()
    context["title"] = title
    context['form'] = form
    context['project'] = settings.PROJECT_TITLE
    if request.method == 'POST':
        rotate_token(request)
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None and not request.user.is_authenticated:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                messages.success(request, message)
                return redirect('home')
        else:
            message = 'Login failed! Email and password records do not exist.'
            messages.error(request, message)
            return render(request, "accounts/login_form.html", context)
    else:
        rotate_token(request)
        return render(request, "accounts/login_form.html", context)

