from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserRegisterForm
from accounts.models import User
from django.views.generic import View
from django.conf import settings
from django.middleware.csrf import rotate_token


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/registration_form.html'
    project_name = settings.PROJECT_TITLE

    def get(self, request):
        form = self.form_class(None)
        context = dict()
        context['form'] = form
        context['project'] = self.project_name
        rotate_token(self.request)
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = dict()
        if form.is_valid():
            password = request.POST.get('password')
            emai = request.POST.get('email')
            first_nam = request.POST.get('first_name')
            last_nam = request.POST.get('last_name')
            try:
                existing_user = User.objects.get(email=emai)
                messages.info(self.request, 'User already Exists! Proceed to Login.')
                return redirect('login')
            except ObjectDoesNotExist:
                user = User(
                    email=emai,
                    first_name=first_nam,
                    last_name=last_nam
                )
                user.set_password(password)
                user.save()
                messages.success(self.request,'New User Added Successfully. Proceed to login.')
                return redirect('login')
        else:
            messages.error(self.request, 'User Not Added. Restart User Registration Process!')
            context['form'] = form
            context['project'] = self.project_name
            rotate_token(self.request)
            return render(request, self.template_name, context)


    def get_context_data(self, **kwargs) :
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        return context
