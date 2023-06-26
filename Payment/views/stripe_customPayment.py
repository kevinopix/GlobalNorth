from django.conf import settings
from django.views.generic import TemplateView
from services.models import Package, Service


class CustomPaymentView(TemplateView):
    template_name = "services/custom_payment.html"

    def get_context_data(self, **kwargs):
        # product = Product.objects.get(name="Test Product")
        # prices = Price.objects.filter(product=product)
        product = Package.objects.get(id=kwargs['pk'])
        context = super(CustomPaymentView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLISHABLE_KEY
        })
        try:
            packages = Package.objects.filter(is_active=True)
            context.update({
                "packages": packages
            })
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