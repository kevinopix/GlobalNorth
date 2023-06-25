from django.core.exceptions import ValidationError
from django.db import models
from tinymce.models import HTMLField
import random


def validate_bullet_briefs(value):
    if "--" in value:
        return value
    else:
        raise ValidationError("There has to be more than one value and they have to be separated by two dashes")


class Package(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=30, null=True, blank=True)
    description = HTMLField()
    bullet_briefs = models.TextField(null=True, blank=True,
                                     help_text="Add each bullet sepeare by two dashes '--'",
                                     validators=[validate_bullet_briefs])
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "Package"

    def get_absolute_url(self):
        return f"/services/package/{self.pk}/view/"


    @property
    def package_color(self):
        # color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)]) for j in range(50)]
        return color[int(self.pk)*5]

    @property
    def list_bullets(self):
        try:
            vals = self.bullet_briefs.split('--')
            vals = [x.strip()[:30] for x in vals]
        except:
            vals = []
        return vals

    @property
    def price(self):
        try:
            from service.models import Price
            price = int(Price.objects.get(product__pk=self.pk).price)
            # print(price)
        except Exception as e:
            # print(e)
            price = 0
        return price
