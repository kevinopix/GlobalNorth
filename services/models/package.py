from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "Package"

    def get_absolute_url(self):
        return f"/services/package/{self.pk}/view/"

    @property
    def stripe_price_id(self):
        return "custom_" + str(self.price)


# class Price(models.Model):
#     product = models.ForeignKey(Package, on_delete=models.CASCADE)
#     stripe_price_id = models.CharField(max_length=100)
#     price = models.IntegerField(default=0)  # cents
#
#     def get_display_price(self):
#         return "{0:.2f}".format(self.price / 100)