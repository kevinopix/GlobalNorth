from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from services.models import Package


class PaymentFailedView(LoginRequiredMixin,generic.TemplateView):
    template_name = "payment/failed_pay.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentFailedView, self).get_context_data(**kwargs)
        try:
            packages = Package.objects.all()
            context['packages'] = packages
        except:
            pass
        return context