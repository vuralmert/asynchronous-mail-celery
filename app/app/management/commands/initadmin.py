from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser using the configured environment variables.'

    def handle(self, *args, **options):
        superuser_username = config('DJANGO_SUPERUSER_USERNAME')
        superuser_email = config('DJANGO_SUPERUSER_EMAIL')
        superuser_password = config('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=superuser_username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Creating superuser account for {superuser_username} ({superuser_email})'))
            User.objects.create_superuser(
                email=superuser_email, username=superuser_username, password=superuser_password)
        else:
            self.stdout.write(self.style.WARNING('Admin account has already been initialized.'))
