from django.db import models


class Terms(models.Model):
    terms_and_conditions = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.terms_and_conditions

    class Meta:
        verbose_name = 'Terms and Conditions'
        verbose_name_plural = 'Terms and Conditions'