import stripe
from django.conf import settings
from django.http import JsonResponse
# from django.shortcuts import redirect
from django.urls import reverse
# from django.utils.decorators import method_decorator
# from django.views import View
from django.views.decorators.csrf import csrf_exempt
from services.models import Package

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request, **kwargs):
    if request.method == 'GET':
        package = Package.objects.get(id=kwargs["pk"])
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                # client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=request.build_absolute_uri(
                    reverse('success_stripe_pay')
                ) + "?session_id={CHECKOUT_SESSION_ID}",
                # success_url=domain_url + 'pay/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('failed_stripe_pay')),
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': str(package.name),
                        'quantity': 1,
                        'currency': 'usd',
                        'description': str(package.name),
                        'amount': str(package.price * 100),
                    }
                ]
            )
            # print(checkout_session)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})