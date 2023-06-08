from django.urls import path
from .views import *

urlpatterns = [
    path('config/', stripe_config, name="stripe-config"),
    # path('create-checkout-session/<int:pk>/', create_checkout_session, name='create-checkout-session'),
    path('create-payment-intent/<int:pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('services/custom-payment/<int:pk>/', CustomPaymentView.as_view(), name='custom-payment'),
    path('pay/success/', PaymentSuccessView.as_view(), name='success_stripe_pay'),
    path('pay/cancel/', PaymentCancelView.as_view(), name='cancel_stripe_pay'),
    path('pay/failed/', PaymentFailedView.as_view(), name='failed_stripe_pay'),
    path('create-checkout-session/<pk>/', CreateStripeCheckoutSessionView.as_view(), name='create-checkout-session'),
]