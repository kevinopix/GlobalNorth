from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="kevinopix@gmail.com").exists():
            User.objects.create_superuser(
                email='kevinopix@gmail.com',
                password='pa00037011'
            )
        elif not User.objects.filter(email="omwonoclinton38@gmail.com").exists():
            User.objects.create_superuser(
                email='omwonoclinton38@gmail.com',
                password='pa00037011'
            )
        elif not User.objects.filter(email="rwey007@gmail.com").exists():
            User.objects.create_superuser(
                email='rwey007@gmail.com',
                password='pa00037011'
            )