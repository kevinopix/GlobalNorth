from django.db import models
from accounts.models import UserProfile
from services.models import Package


class PaymentDetail(models.Model):
    # id = models.BigAutoField(primary_key=True)
    customer_email = models.ForeignKey(to=UserProfile, verbose_name='Customer Email', on_delete=models.PROTECT)
    package = models.ForeignKey(to=Package, verbose_name='Package',on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False,verbose_name='Payment Status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{a} --- {b} --- {c} --- {d}".format(a=str(self.id),
                                            b=str(self.customer_email.email),
                                            c=str(self.amount),
                                            d=str(self.package.name))