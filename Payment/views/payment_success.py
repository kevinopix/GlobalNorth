import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from Payment.models import PaymentDetail
from services.models import Package, Service
from accounts.models import UserProfile


class PaymentSuccessView(LoginRequiredMixin,generic.TemplateView):
    template_name = "payment/success_pay.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        # print(session_id)
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        # print(session)
        # amount_paid = session["display_items"][0]['amount']
        amount_paid = session["amount_total"]
        package_id = session["metadata"]["product_id"]
        product = Package.objects.get(id=package_id)
        # order = get_object_or_404(PaymentDetail, stripe_payment_intent=session.payment_intent)
        logged_user = self.request.user
        try:
            userprofile = UserProfile.objects.get(user__pk=logged_user.pk)
            order = PaymentDetail()
            order.customer_email = userprofile
            order.package = product
            # order.package_id = product.id
            order.stripe_payment_intent = session['payment_intent']
            order.amount = amount_paid / 100
            order.save()
            order.has_paid = True
            order.save()
            return render(request, self.template_name)
        except:
            messages.warning(self.request,"User Profile Does NOT exist. Create one before proceeding!")
            return redirect('/accounts/profile/new')

    def get_context_data(self, **kwargs):
        context = super(PaymentSuccessView, self).get_context_data(**kwargs)
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