import json, stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from services.models import Package
from accounts.models import UserProfile
from Payment.models import PaymentDetail


@csrf_exempt
@login_required
def create_checkout_session(request, **kwargs):
    request_data = json.loads(request.body)
    product = get_object_or_404(Package, pk=kwargs['id'])
    stripe.api_key = settings.STRIPE_SECRET_KEY
    logged_user = request.user
    try:
        user = UserProfile.objects.get(user__pk=logged_user.pk)
        try:
            checkout_session = stripe.checkout.Session.create(
                customer_email=user.email,
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': product.name,
                            },
                            'unit_amount': int(product.price * 100),
                        },
                        'quantity': 1,
                    }
                ],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('success_pay')
                ) + "?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri(reverse('failed_pay')),
            )
        except Exception as e:
            print(e)
        order = PaymentDetail()
        order.customer_email = user
        order.product = product
        order.stripe_payment_intent = checkout_session['payment_intent']
        order.amount = int(product.price * 100)
        order.save()
        return JsonResponse({'sessionId': checkout_session.id})
    except Http404:
        messages.error(request,"User profile does not exist!")
        return redirect("/accounts/profile/new")
