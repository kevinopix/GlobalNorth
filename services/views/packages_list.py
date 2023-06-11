# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Package
from django.views import generic
from django.conf import settings
from django.middleware.csrf import rotate_token


class PackagesListView(generic.TemplateView):
    template_name = 'services/list_package.html'
    project_name = settings.PROJECT_TITLE
    model = Package
    page_title = "Packages List"

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data()
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
            rotate_token(self.request)
            return render(self.request, self.template_name, context)
        except Http404:
            print("Not exist")
            messages.error(self.request, "Package Does NOT exist.")
            return redirect('/')

    def get_context_data(self, **kwargs) :
        context = super(PackagesListView, self).get_context_data(**kwargs)
        context['project'] = self.project_name
        context['page_title'] = self.page_title
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
        except:
            pass
        return context
