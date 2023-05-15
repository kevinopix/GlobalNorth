from django.views import generic


class PaymentCancelView(generic.TemplateView):
    template_name = "payment/cancel_pay.html"