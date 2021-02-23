from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()
A = Account()

for i in range(100):
    A.Amount = int(fake.random_int())
    A.Creating_Date = fake.date()
    A.number_id = 2
    A.save()