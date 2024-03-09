import os
import django
import random

from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anc_test_task.settings')
django.setup()

from main_app.models import Employee

fake = Faker()

# create top menager without boss
top_management = [Employee.objects.create(
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    position=fake.job(),
    hire_date=fake.date_this_decade(),
    email=fake.email(),
    boss=None
) for _ in range(10)]
print('create all managers')

# create other levels with depends on counts of boss and subordinate
for i in range(6):
    for _ in range(2 ** i): # for 50K change 2 to 10
        boss = random.choice(top_management) if i > 0 else None
        employee = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=fake.job(),
            hire_date=fake.date_this_decade(),
            email=fake.email(),
            boss=boss
        )
        if i < 5:  # limiting count of subordinate, only for high level
            for _ in range(random.randint(1, 10)):
                subordinate = Employee.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    position=fake.job(),
                    hire_date=fake.date_this_decade(),
                    email=fake.email(),
                    boss=employee
                )
