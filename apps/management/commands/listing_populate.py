from django.core.management.base import BaseCommand
from faker import Faker
from apps.models import Listing, User, Category  # User va Category modellaringizni import qiling

class Command(BaseCommand):
    help = "Populates the database with listings"

    def add_arguments(self, parser):
        parser.add_argument("user", type=int)

    def handle(self, *args, **options):
        listings = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['user']):
            random_user = User.objects.order_by('?').first()
            random_category = Category.objects.order_by('?').first()
            listings.append(Listing(
                owner=random_user,
                category=random_category,
                description=f.text(max_nb_chars=255),
                place=f.address(),
                price=f.random_number(digits=3) * 1000,
                price_currency=f.random_element(elements=[choice[0] for choice in Listing.Currency.choices]),
                price_type=f.random_element(elements=[choice[0] for choice in Listing.PriceType.choices]),
                price_period_unit=f.company_suffix(),
                room=max(1, f.random_number(digits=1) * 12),
                is_price_auction=f.boolean(),
                square=max(1, f.random_number(digits=1, fix_len=True)),
                floor=max(1, f.random_number(digits=1, fix_len=True)),
                floor_total=max(1, f.random_number(digits=1, fix_len=True)),
                is_new_building=f.boolean(),
                repair=f.random_element(elements=[choice[0] for choice in Listing.RepairType.choices]),
                foundation=f.random_element(elements=[choice[0] for choice in Listing.FoundationType.choices]),
                residential_complex_id=None,
                moderation_status=f.random_element(elements=[choice[0] for choice in Listing.MSType.choices]),
                urgently_expired_at=f.date_time_ad(),
                verified_expired_at=f.date_time_ad(),
                premium_expired_at=f.date_time_ad(),
                vip_expired_at=f.date_time_ad(),
                views=f.random_number(digits=2) * 1000,
                favorites=f.random_number(digits=2) * 100,
                is_vip=f.boolean(),
                is_premium=f.boolean(),
                is_urgently=f.boolean()
            ))

        Listing.objects.bulk_create(listings)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['user']} listings")
        )
