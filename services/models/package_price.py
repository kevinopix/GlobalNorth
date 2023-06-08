from django.db import models
from services.models import Package


class Price(models.Model):
    product = models.ForeignKey(Package, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} {self.price}"

    @property
    def stripe_price_id(self):
        return "custom_" + str(self.price)