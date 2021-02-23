from santander.models import User
from santander.models import Account
from faker import Faker
fake = Faker()

import random
L1 = random.sample(range(1, 21), 20) # Get random number for Fk


for i in range(20): #generata 20 rows of fake data for Account
    a = fake.name()
    b = fake.name()
    c = fake.address()
    num = L1[0+i]       # Get random number to assign account pk
    d = Account(id=num) # Get Account PK
    e = fake.random_int(min=16, max=110)
    f = fake.company()
    g = fake.random_int(min=0, max=1)
    h = fake.date()
    A = User(Name=a, Surname=b, Address=c, Account=d, Age=e, Company=f, Status=g, Creating_Date=h)
    A.save()
    i += 1





