import pprint

from django.contrib.auth.models import User
from django.core.management import BaseCommand

pp = pprint.PrettyPrinter(indent=4)


class Command(BaseCommand):
    help = "Check if db is necessary"

    def handle(self, *args, **options):
        if not User.objects.filter(pk=1).exists():
            return "False"
        else:
            return "True"
