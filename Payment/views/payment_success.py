import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from Payment.models import PaymentDetail
from services.models import Package
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
        amount_paid = session["display_items"][0]['amount']
        package_name = session["display_items"][0]["custom"]['name']
        product = Package.objects.get(name=package_name)
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
            messages.warning("User Profile Does NOT exist. Create one before proceeding!")
            return redirect('/accounts/profile/new')