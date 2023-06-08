import stripe
import json
from django.http import JsonResponse
from django.views import View
from services.models import Package


class StripeIntentView(View):

    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            print(req_json)
            customer = stripe.Customer.create(email=req_json['email'])
            product = Package.objects.get(id=kwargs["pk"])
            # price = Price.objects.get(id=self.kwargs["pk"])
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "product_id": product.id
                }
            )
            print(intent['client_secret'])
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})