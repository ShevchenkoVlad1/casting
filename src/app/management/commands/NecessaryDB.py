# temp imports
import pprint
from datetime import datetime

from django.core.management import BaseCommand

from user.models import User

pp = pprint.PrettyPrinter(indent=4)


class Command(BaseCommand):
    help = "Check if db is necessary"

    def handle(self, *args, **options):
        if not User.objects.filter(pk=1).exists():
            self.write('Table "user" does not exist.')
            return False
        else:
            self.write('Table "user" already exists.')
            return True

    def write(self, string):
        self.stdout.write("[%s] %s" % (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            string,
        ))
