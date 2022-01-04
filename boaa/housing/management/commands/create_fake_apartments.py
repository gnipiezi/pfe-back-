import os
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker
from housing.models import Apartment, Profile


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('num_apartments', default=10, type=int)
        parser.add_argument('superuser_id', type=int)

    def handle(self, *args, **options):
        fake = Faker()

        try:
            default_user = User.objects.get(pk=options['superuser_id'])
            Profile.objects.create(
                owner=default_user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                address=fake.address()
            )

            default_site = Apartment.objects.create(
                owner=default_user,
                site=None,
                address=fake.address(),
                created_date=datetime.datetime.now()
            )

            for _ in range(options['num_apartments']):
                profile = fake.simple_profile()
                owner = User.objects.create_user(
                    username=profile["username"],
                    email=profile["mail"],
                    password=os.environ.get("DEFAULT_LOGIN_PASSWORD", "123supersecure")
                )
                s = profile["name"].split(' ')
                first_name, last_name = s if len(s) >= 2 else profile["name"], profile["name"]
                Profile.objects.create(
                    owner=owner,
                    first_name=first_name,
                    last_name=last_name,
                    address=profile["address"]
                )

                Apartment.objects.create(
                    owner=owner,
                    site=default_site,
                    address=fake.address(),
                    created_date=datetime.datetime.now()
                )
            self.stdout.write(self.style.SUCCESS('Successfully created apartments'))
        except User.DoesNotExist:
            raise CommandError('Superuser "%s" does not exist' % options["user_id"])
