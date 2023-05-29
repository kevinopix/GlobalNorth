from django.views import generic
from services.models import Package


class PaymentCancelView(generic.TemplateView):
    template_name = "payment/cancel_pay.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentCancelView, self).get_context_data(**kwargs)
        try:
            packages = Package.objects.filter(is_active=True)
            context['packages'] = packages
        except:
            pass
        return context