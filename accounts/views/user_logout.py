from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.conf import settings
from django.middleware.csrf import rotate_token
from django.views import generic


class UserLogoutView(generic.TemplateView):
    title = 'Logout'
    project = settings.PROJECT_TITLE
    def get(self, request, *args, **kwargs):
        logout(request)
        rotate_token(request)
        context = self.get_context_data()
        context["title"] = self.title
        context['project'] = self.project
        rotate_token(request)
        return render(request, "accounts/logout_form.html", context)

    def get_context_data(self, **kwargs) :
        context = super(UserLogoutView, self).get_context_data(**kwargs)
        return context
