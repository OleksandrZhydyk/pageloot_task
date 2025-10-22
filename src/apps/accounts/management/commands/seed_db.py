import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from apps.accounts.models import User


class Command(BaseCommand):
    help = "Load JSON fixture into DB only if the DB is empty"

    def handle(self, *args, **kwargs):
        if User.objects.exists():
            self.stdout.write(self.style.SUCCESS("Database already populated. Skipping fixture."))
            return

        fixture_path = os.path.join(settings.BASE_DIR, "db.json")
        if not os.path.exists(fixture_path):
            self.stdout.write(self.style.ERROR(f"Fixture not found: {fixture_path}"))
            return

        call_command("loaddata", fixture_path)
        self.stdout.write(self.style.SUCCESS("Database populated from JSON fixture!"))
