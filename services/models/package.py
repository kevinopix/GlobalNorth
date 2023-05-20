from django.db import models
from tinymce.models import HTMLField


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = HTMLField()
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "Package"

    def get_absolute_url(self):
        return f"/services/package/{self.pk}/view/"

    @property
    def stripe_price_id(self):
        return "custom_" + str(self.price)

