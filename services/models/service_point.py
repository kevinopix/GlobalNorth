from django.db import models
from services.models import Service


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    bullet_item = models.CharField(max_length=200)

    def __str__(self):
        return "{a} ---- {b}".format(a=str(self.service.name), b=str(self.bullet_item))