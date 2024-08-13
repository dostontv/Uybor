from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import User, Category


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("category", type=int)

    def handle(self, *args, **options):
        category = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['category']):
            category.append(Category(
                name= f.name(),
                # parent_id=f.null_boolean(),
                is_active= f.boolean(),
                weight=f.random_digit(),
                operation_type=f.random_choices(elements=Category.OperationType.choices, length=1)[0][0]
            ))

        Category.objects.bulk_create(category)
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['category']} categories")
        )
