from django.db import models


class Mission(models.Model):
    mission_text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mission_text[:20]