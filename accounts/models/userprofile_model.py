from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    # products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.email