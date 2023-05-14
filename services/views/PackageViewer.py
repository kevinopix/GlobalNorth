# from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Package
from django.views import generic
from django.conf import settings
from django.middleware.csrf import rotate_token


class PackageViewerView(generic.TemplateView):
    template_name = 'services/view_package.html'
    project_name = settings.PROJECT_TITLE
    model = Package
    page_title = "Package"

    def get(self, request, *args, **kwargs):
        package_pk = kwargs['pk']
        try:
            package = get_object_or_404(self.model, pk=package_pk)
            # if package:
            context = self.get_context_data()
            context['package'] = package
            rotate_token(self.request)
            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            messages.error(self.request, "Package Does NOT exist.")
            return redirect('/')

    def get_context_data(self, **kwargs) :
        context = super(PackageViewerView, self).get_context_data(**kwargs)
        context['project'] = self.project_name
        context['page_title'] = self.page_title
        return context
