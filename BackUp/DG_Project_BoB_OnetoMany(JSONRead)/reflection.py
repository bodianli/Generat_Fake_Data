from BankData.models import User    # Change(1)
from faker import Faker
import random

fake = Faker()


class UserFactory(object):

    def __init__(self):
        self.user = User()          # Change(1)

    def set_fullname(self):
        self.user.fullname = fake.name()        # Change(1)

    def set_surname(self):
        self.user.surname = fake.name()           # Change(1)

    def set_address(self):
        self.user.address = fake.address()      # Change(1)

    def set_age(self):
        self.user.age = fake.random_int(min=18, max=100)    # Change(1)

    def set_company(self):
        self.user.company = fake.company()                     # Change(1)

    def set_status(self):
        self.user.status = 'Active' if fake.random_int(min=0, max=1) == 1 else 'Inactive' # Change(1)

    def set_creatingdate(self):
        self.user.creatingdate = fake.date() # Change(1)

    def save(self):
        self.user.save()

    method_map = {
        "1": set_fullname,
        "2": set_surname,
        "3": set_address,
        "4": set_age,
        "5": set_company,
        "6": set_status,
        "7": set_creatingdate,
    }


rows = int(input('Generated row number: '))
for k, v in UserFactory.method_map.items():
    print('{}: {}'.format(k, v.__name__))
column_numbers = input('Columns to generate (separate with ","): ').split(',')

for _ in range(rows):
    user_factory = UserFactory()
    for column_number in column_numbers:
        user_factory.method_map[column_number](user_factory)
    user_factory.save()
