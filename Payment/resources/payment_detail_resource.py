from import_export import resources
from Payment.models import PaymentDetail


class PaymentDetailResource(resources.ModelResource):

    class Meta:
        model = PaymentDetail