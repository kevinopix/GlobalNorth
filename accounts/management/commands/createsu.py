from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="kevinopixadm@gmail.com").exists():
            User.objects.create_superuser(
                username='kevinopixadm@gmail.com',
                password='pa00037011'
            )
            new_user = User.objects.get(email="kevinopixadm@gmail.com")
            new_user.first_name = "Kevin"
            new_user.last_name = "Okome"
            new_user.save()
            # User.objects.create_superuser("admin", "admin@admin.com", "admin")