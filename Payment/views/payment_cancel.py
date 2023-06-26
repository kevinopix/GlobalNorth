from django.views import generic
from services.models import Package, Service


class PaymentCancelView(generic.TemplateView):
    template_name = "payment/cancel_pay.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentCancelView, self).get_context_data(**kwargs)
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