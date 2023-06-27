from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a default user using the configured environment variables.'

    def handle(self, *args, **options):
        defaultuser_username = config('DJANGO_DEFAULTUSER_USERNAME')
        defaultuser_email = config('DJANGO_DEFAULTUSER_EMAIL')
        defaultuser_password = config('DJANGO_DEFAULTUSER_PASSWORD')

        if not User.objects.filter(username=defaultuser_username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Creating normal user account for {defaultuser_username} ({defaultuser_email})'))
            User.objects.create_user(
                email=defaultuser_email, username=defaultuser_username, password=defaultuser_password)
        else:
            self.stdout.write(self.style.WARNING('Default user account has already been initialized.'))
