from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import Category


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("category", type=int)

    def handle(self, *args, **options):
        category = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['category']):
            random_category = Category.objects.order_by('?').first()
            category.append(Category(
                name=f.name(),
                parent_id=random_category,
                is_active=f.boolean(),
                weight=f.random_digit(),
                operation_type=f.random_choices(elements=Category.OperationType.choices, length=1)[0][0]
            ))

        Category.objects.bulk_create(category)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['category']} categories")
        )
