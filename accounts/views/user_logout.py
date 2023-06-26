from django.shortcuts import render
from django.contrib.auth import logout
from django.conf import settings
from django.middleware.csrf import rotate_token
from django.views import generic
from services.models import Package, Service


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
        context["page_title"] = self.title
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
        except:
            pass
        try:
            services = Service.objects.filter(is_active=True)
            context['services'] = services
        except:
            pass
        try:
            from testimonials.models import Testimony
            testimonials = Testimony.objects.filter(is_active=True)
            context['testimonials'] = testimonials
        except:
            pass
        return context
