from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    terms_conditions_accepted = models.BooleanField(default=False)
    date_terms_accepted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # date_created = models.DateTimeField(auto_now_add=True)
    # products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return f"/accounts/profile/{self.pk}/view"