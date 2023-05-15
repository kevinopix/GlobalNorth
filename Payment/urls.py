from django.urls import path
from .views import *

urlpatterns = [
    # path('', ProductListView.as_view(), name='home'),
    # path('create/', ProductCreateView.as_view(), name='create'),
    # path('detail/<id>/', ProductDetailView.as_view(), name='detail'),
    # path('history/', OrderHistoryListView.as_view(), name='history'),
    # path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('config/', stripe_config),
    path('create-checkout-session/<int:pk>/', create_checkout_session, name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('pay/success/', PaymentSuccessView.as_view(), name='success_stripe_pay'),
    path('pay/cancel/', PaymentCancelView.as_view(), name='cancel_stripe_pay'),
    path('pay/failed/', PaymentFailedView.as_view(), name='failed_stripe_pay'),
]