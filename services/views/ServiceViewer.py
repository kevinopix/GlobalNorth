# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Package, Service, ServiceItem
from django.views import generic
from django.conf import settings
from django.middleware.csrf import rotate_token


class ServiceViewerView(generic.TemplateView):
    template_name = 'services/view_service.html'
    project_name = settings.PROJECT_TITLE
    model = Service
    page_title = "Service"

    def get(self, request, *args, **kwargs):
        service_pk = kwargs['pk']
        context = self.get_context_data()
        try:
            service = get_object_or_404(self.model, pk=service_pk, is_active=True)
            context["serviceitems"] = ServiceItem.objects.filter(service=service)
            if service.is_active:
                context['service'] = service
                rotate_token(self.request)
                return render(self.request, self.template_name, context)
        except Http404:
            print("Not exist")
            messages.error(self.request, "Service Does NOT exist.")
            return redirect('/')

    def get_context_data(self, **kwargs) :
        context = super(ServiceViewerView, self).get_context_data(**kwargs)
        context['project'] = self.project_name
        context['page_title'] = self.page_title
        if self.request.user.is_authenticated:
            context['email'] = self.request.user.email
        try:
            packages = Package.objects.all()
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
