from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "Package"