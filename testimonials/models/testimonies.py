from django.db import models


class Testimony(models.Model):
    testimony_text = models.TextField()
    testimony_by = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{a} by {b}.".format(a=str(self.testimony_text)[:20], b=self.testimony_by)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"