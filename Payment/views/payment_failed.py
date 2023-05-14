from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class PaymentFailedView(LoginRequiredMixin,generic.TemplateView):
    template_name = "payment/failed_pay.html"