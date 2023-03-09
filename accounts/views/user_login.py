from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.middleware.csrf import rotate_token
from django.views import generic


class UserLoginView(generic.TemplateView):
    title = "Login"
    project = settings.PROJECT_TITLE
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["title"] = self.title
        context['project'] = self.project
        rotate_token(request)
        form = UserLoginForm()
        context['form'] = form
        return render(request, "accounts/login_form.html", context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            print(username)
            user = authenticate(
                username=username,
                password=form.cleaned_data['password']
            )
            if user is not None and not self.request.user.is_authenticated:
                login(self.request, user)
                message = f'Hello {username}! You have been logged in'
                messages.success(self.request, message)
                return redirect('home')
        else:
            message = 'Login failed! Email and password records do not exist.'
            messages.error(self.request, message)
            context = self.get_context_data()
            context["title"] = self.title
            context['project'] = self.project
            rotate_token(request)
            form = UserLoginForm()
            context['form'] = form
            return render(self.request, "accounts/login_form.html", context)

    def get_context_data(self, **kwargs) :
        context = super(UserLoginView, self).get_context_data(**kwargs)
        return context
