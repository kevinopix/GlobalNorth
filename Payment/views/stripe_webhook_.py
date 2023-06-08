import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from accounts.models import UserProfile
from services.models import Package


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Package.objects.get(id=product_id)

        # send_mail(
        #     subject="Here is your product",
        #     message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
        #     recipient_list=[customer_email],
        #     from_email="matt@test.com"
        # )

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Package.objects.get(id=product_id)

        # send_mail(
        #     subject="Here is your product",
        #     message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
        #     recipient_list=[customer_email],
        #     from_email="matt@test.com"
        # )
    return HttpResponse(status=200)

# @csrf_exempt
# def stripe_webhook(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#     logged_user = request.user
#
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     try:
#         user = request.user
#         userprofile = UserProfile.objects.get(user__pk=user.pk)
#         if userprofile:
#             if event['type'] == 'checkout.session.completed':
#                 session = event['data']['object']
#                 payment_intent = session.get("payment_intent")
#                 itemz = session.get("display_items")
#                 package = itemz["custom"]["name"]
#                 return HttpResponse(status=200)
#         else:
#             client_reference_id = UserProfile.objects.get(user__pk=logged_user)
#             if client_reference_id is None:
#                 return redirect('/accounts/login')
#     except Exception as e:
#         return redirect('/accounts/profile/new')

