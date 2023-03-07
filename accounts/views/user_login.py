from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from accounts.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.template.context_processors import csrf


def login_view(request):
    title = "Login"
    form = UserLoginForm()
    context = {}
    context["title"] = title
    context['form'] = form
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print(request.session.items())
        if form.is_valid():
            print('yes valid')
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            print(user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return HttpResponseRedirect(reverse('home'))
            else:
                message = 'Login failed!'
                return render(request, "accounts/login_form.html", context)
    else:
        return render(request, "accounts/login_form.html", context)

