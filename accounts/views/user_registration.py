from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib import messages
import pandas as pd
from accounts.forms import UserRegisterForm
from accounts.models import User
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if self.request.method == 'POST':
            password = request.POST.get('password')
            emai = request.POST.get('email')
            first_nam = request.POST.get('first_name')
            last_nam = request.POST.get('last_name')
            listi = pd.DataFrame(User.objects.values('email'))['email'].tolist()
            if emai not in listi:
                # User.objects.get_or_create(
                #     email=emai,
                #     password = make_password(password),
                #     first_name = first_nam,
                #     last_name = last_nam
                # )
                user = User(
                    email=emai,
                    first_name = first_nam,
                    last_name = last_nam
                )
                user.set_password(password)
                user.save()
                messages.success(self.request,'New User Added Successfully. Proceed to login.')
                return HttpResponseRedirect(reverse('login'))
            elif emai in listi:
                messages.error(self.request,'User already Exists! Proceed to Login.')
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(self.request, 'User Not Added. Restart User Registration Process!')
            return render(request, self.template_name, {'form': form})
            # messages.error(self.request,'User Not Added. Repeat ')
            # return HttpResponseRedirect(reverse('login'))

