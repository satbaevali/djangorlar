import random
from datetime import date
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from faker import Faker
from decimal import Decimal

from django.conf import settings
from django.db import transaction

from user.models import CustomUser

fake = Faker()
Faker.seed(0)
random.seed(0)

DEPARTMENTS = ['IT', 'HR', 'Sales', 'Finance']
ROLES = ['admin', 'manager', 'employee']

BATCH_SIZE = 1000
TOTAL = 10000
PASSWORD_PLAIN = "12345"


def random_birthdate():
   
    start = date(1975, 1, 1)
    end = date(2005, 12, 31)
    return fake.date_between(start_date=start, end_date=end)


class Command(BaseCommand):
    help = "Generate 10,000 fake users (bulk_create in batches)."

    def handle(self, *args, **options):
        users_to_create = []
        # Pre-hash password once (efficient)
        hashed_password = make_password(PASSWORD_PLAIN)

        unique_email = fake.unique
        fake_unique = Faker()
        fake_unique.seed_instance(0)

        for i in range(TOTAL):
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Ensure unique email and username
            email = fake.unique.email()
            username = email.split('@')[0] + str(i)  # avoid accidental duplicates
            phone = fake.phone_number()
            city = fake.city()
            country = fake.country()
            department = random.choice(DEPARTMENTS)
            role = random.choice(ROLES)
            birth_date = random_birthdate()
            # salary random between 100_000 and 1_000_000
            salary = random.randint(100_000, 1_000_000)

            user = CustomUser(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                city=city,
                country=country,
                department=department,
                role=role,
                birth_date=birth_date,
                salary=salary,
                is_active=True,
                is_staff=(role == 'admin'),  # optionally
                date_joined=timezone.now(),
                last_login=None,
            )
            # set hashed password value directly
            user.password = hashed_password

            users_to_create.append(user)

            # batch flush
            if len(users_to_create) >= BATCH_SIZE:
                CustomUser.objects.bulk_create(users_to_create, batch_size=BATCH_SIZE)
                self.stdout.write(self.style.SUCCESS(f"Inserted {len(users_to_create)} users..."))
                users_to_create = []

        # remaining
        if users_to_create:
            CustomUser.objects.bulk_create(users_to_create, batch_size=BATCH_SIZE)
            self.stdout.write(self.style.SUCCESS(f"Inserted {len(users_to_create)} users (final batch)."))

        self.stdout.write(self.style.SUCCESS(f"Done — generated {TOTAL} users."))