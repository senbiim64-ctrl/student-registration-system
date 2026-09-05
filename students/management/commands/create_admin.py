import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')

        if not username or not password:
            self.stdout.write(
                self.style.ERROR(
                    'ADMIN_USERNAME and ADMIN_PASSWORD are required'
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f'User {username} already exists'
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'User {username} created successfully'
            )
        )
        