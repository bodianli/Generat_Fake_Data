from santander.models import Account
from faker import Faker
fake = Faker()


for i in range(20): #generata 20 rows of fake data for Account

    b = int(fake.random_int())
    c = fake.date()
    A = Account(Amount=b, Creation_Date= c)
    A.save()


