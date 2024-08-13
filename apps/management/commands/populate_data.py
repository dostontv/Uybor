from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import User


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("user", type=int)

    def handle(self, *args, **options):
        users = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['user']):
            users.append(User(
                first_name=f.name(),
                phone_number=f"998{f.msisdn()[:9]}",
                balance=f.random_number(digits=3) * 1000,
                organization=f.company(),
                type=f.random_choices(elements=User.UserType.choices, length=1)[0][0]
            ))

        User.objects.bulk_create(users)
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['user']} users")
        )
