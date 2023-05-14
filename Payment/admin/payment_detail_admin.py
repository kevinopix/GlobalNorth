from django.contrib import admin
from Payment.models import PaymentDetail
from Payment.resources import PaymentDetailResource
from import_export.admin import ImportExportModelAdmin


class PaymentDetailAdmin(ImportExportModelAdmin):
    model = PaymentDetail
    resource_class = PaymentDetailResource
    list_display = ('id', 'customer_email','package','stripe_payment_intent','amount','has_paid')


admin.site.register(PaymentDetail, PaymentDetailAdmin)