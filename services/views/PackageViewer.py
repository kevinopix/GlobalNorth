# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
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
            if package.is_active:
                context = self.get_context_data()
                context['package'] = package
                try:
                    packages = Package.objects.all()
                    context['packages'] = packages
                except:
                    pass
                rotate_token(self.request)
                return render(self.request, self.template_name, context)
        except Http404:
            print("Not exist")
            messages.error(self.request, "Package Does NOT exist.")
            return redirect('/')

    def get_context_data(self, **kwargs) :
        context = super(PackageViewerView, self).get_context_data(**kwargs)
        context['project'] = self.project_name
        context['page_title'] = self.page_title
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['email'] = self.request.user.email
        return context
