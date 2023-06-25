from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/services/service/{self.pk}/view/"

    @property
    def serviceitems(self):
        try:
            from services.models import ServiceItem
            services = ServiceItem.objects.filter(service__pk=self.pk)
        except Exception as e:
            services = None
        return services