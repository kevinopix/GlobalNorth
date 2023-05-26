import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from accounts.models import UserProfile
from Payment.models import PaymentDetail


@login_required
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    logged_user = request.user

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
        try:
            user = request.user
            userprofile = UserProfile.objects.get(user__pk=user.pk)
            if event['type'] == 'checkout.session.completed':
                session = event['data']['object']
                client_reference_id = UserProfile.objects.get(user__pk=logged_user)
                payment_intent = session.get("payment_intent")
                itemz = session.get("display_items")
                package = itemz["custom"]["name"]
                if client_reference_id is None:
                    return redirect('/accounts/login')
                return HttpResponse(status=200)
        except Exception as e:
            return redirect('/accounts/profile/new')
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)




# @login_required
# def handle_checkout_session(session):
#     # client_reference_id = user's id
#     client_reference_id = session.get("client_reference_id")
#     payment_intent = session.get("payment_intent")
#     itemz = session.get("display_items")
#     package = itemz["custom"]["name"]
#     print(package)
#
#     if client_reference_id is None:
#         # Customer wasn't logged in when purchasing
#         print("User Profile DOES NOT Exist")
#         return redirect('/accounts/login')
#
#     # Customer was logged in we can now fetch the Django user and make changes to our models
#     try:
#         user = User.objects.get(id=client_reference_id)
#         userprofile = UserProfile.objects.get(user__pk=user.pk)
#         print(user.email, "just purchased something.")
#
#         order = PaymentDetail()
#         order.customer_email = userprofile
#         order.product = product
#         order.stripe_payment_intent = checkout_session['payment_intent']
#         order.amount = int(product.price * 100)
#         order.save()
#     except Exception as e:
#         print(e)
