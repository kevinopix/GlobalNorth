from django.shortcuts import render
from django.contrib.auth import authenticate, login
from accounts.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.template.context_processors import csrf


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    # if form.is_valid():
    if request.method == 'POST':
        emai = request.POST.get('email')
        passwor = request.POST.get('password')
        # if passwor != 'wegot2020':
        user = authenticate(request,email=emai, password=passwor)
        # request.session['SESSION_KEY'] = user._meta.pk.value_to_string(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request,"Are you a registered User and or Researcher?")
            return HttpResponseRedirect(reverse('register'))
        # else:
        #     return HttpResponseRedirect(reverse('password_reset'))
    context = {"form": form, "title": title}
    context.update(csrf(request))
    return render(request, "accounts/login_form.html", context)

