from BankData.models import Account, User
from faker import Faker
import random


fake = Faker()
fk = [i for i in range(20)]

for i in range(100):
    b = int(fake.random_int())
    c = fake.date()
    e = random.choice(fk)
    A = Account(Amount=b, Creating_Date=c, number_id=e)
    A.save()


