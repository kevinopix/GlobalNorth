from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="kevinopixadm@gmail.com").exists():
            new_user = User()
            new_user.email = "kevinopixadm@gmail.com"
            new_user.first_name = "Kevin"
            new_user.last_name = "Okome"
            new_user.password = "pa00037011"
            new_user.is_staff = True
            new_user.is_superuser = True
            new_user.save()
            # User.objects.create_superuser("admin", "admin@admin.com", "admin")