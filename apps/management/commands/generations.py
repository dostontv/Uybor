from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import User, Category, Listing


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    faker = Faker()

    def add_arguments(self, parser):
        parser.add_argument('-u', "--user", type=int)
        parser.add_argument('-c', "--category", type=int)
        parser.add_argument('-l', "--listing", type=int)

    def _user(self, n: int):
        User.objects.bulk_create([
            User(
                first_name=self.faker.name(),
                phone_number=f"998{self.faker.msisdn()[:9]}",
                balance=self.faker.random_number(digits=3) * 1000,
                organization=self.faker.company(),
                password=self.faker.password(),
                type=self.faker.random_choices(elements=User.UserType.choices, length=1)[0][0]
            ) for _ in range(n)
        ])

    def _category(self, n: int):
        category = []
        for _ in range(n):
            random_category = Category.objects.order_by('?').first()
            category.append(Category(
                name=self.faker.name(),
                parent_id=random_category,
                is_active=self.faker.boolean(),
                weight=self.faker.random_digit(),
                operation_type=self.faker.random_choices(elements=Category.OperationType.choices, length=1)[0][0]
            ))
        Category.objects.bulk_create(category)

    def _listing(self, n: int):
        listings = []
        for _ in range(n):
            random_user = User.objects.order_by('?').first()
            random_category = Category.objects.order_by('?').first()
            listings.append(Listing(
                owner=random_user,
                operation_type=self.faker.random_element(
                    elements=[choice[0] for choice in Listing.OperationType.choices]),
                category=random_category,
                description=self.faker.text(max_nb_chars=255),
                place=self.faker.address(),
                price=self.faker.random_number(digits=3) * 1000,
                price_currency=self.faker.random_element(
                    elements=[choice[0] for choice in Listing.Currency.choices]),
                price_type=self.faker.random_element(elements=[choice[0] for choice in Listing.PriceType.choices]),
                price_period_unit=self.faker.company_suffix(),
                room=max(1, self.faker.random_number(digits=1) * 12),
                is_price_auction=self.faker.boolean(),
                square=max(1, self.faker.random_number(digits=1, fix_len=True)),
                floor=max(1, self.faker.random_number(digits=1, fix_len=True)),
                floor_total=max(1, self.faker.random_number(digits=1, fix_len=True)),
                is_new_building=self.faker.boolean(),
                repair=self.faker.random_element(elements=[choice[0] for choice in Listing.RepairType.choices]),
                foundation=self.faker.random_element(
                    elements=[choice[0] for choice in Listing.FoundationType.choices]),
                residential_complex_id=None,
                moderation_status=self.faker.random_element(
                    elements=[choice[0] for choice in Listing.MSType.choices]),
                urgently_expired_at=self.faker.date_time_ad(),
                verified_expired_at=self.faker.date_time_ad(),
                premium_expired_at=self.faker.date_time_ad(),
                vip_expired_at=self.faker.date_time_ad(),
                views=self.faker.random_number(digits=2) * 1000,
                favorites=self.faker.random_number(digits=2) * 100,
                is_vip=self.faker.boolean(),
                is_premium=self.faker.boolean(),
                is_urgently=self.faker.boolean(),
                is_active=self.faker.boolean()
            ))

        Listing.objects.bulk_create(listings)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Populating database..."))

        case = {'user', 'category', 'listing'}
        for m in case.intersection(options):
            if options[m]:
                getattr(self, f"_{m}")(options[m])
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully populated {options[m]} {m}")
                )
