import os

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anc_test_task.settings')
django.setup()

from main_app.models import Employee


def generate_fake_employees():
    fake = Faker()

    # Создаем топ-менеджмент (1 уровень)
    for _ in range(10):  # Для примера создаем 10 топ-менеджеров
        boss = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=fake.job(),
            boss=None,
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            email=fake.email()
        )
        create_hierarchy(boss, fake, level=2, max_level=7)


def create_hierarchy(parent, fake, level, max_level):
    if level > max_level:
        return

    # Создаем подчиненных для текущего руководителя (parent)
    for _ in range():  # Для примера создаем 10 подчиненных на каждом уровне
        subordinate = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=fake.job(),
            boss=parent,
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            email=fake.email()
        )
        create_hierarchy(subordinate, fake, level + 1, max_level)

0
if __name__ == '__main__':
    generate_fake_employees()
