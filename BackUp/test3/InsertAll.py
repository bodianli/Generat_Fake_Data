from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()
A = Account()
U = User()

number1 = eval(input("How many Fake data you want for User?"))
number2 = eval(input("How many Fake data you want for Account?"))

fk = [i for i in range(number1)]
fk

def insert_fake_data(num):
    count = 0
    while count < number1:
        A.AMO = int(fake.random_int())
        A.DAT = fake.date()
        A.ID = random.choice(fk)
        A.save()
        count += 1
    return

'''
count = 0
while count < 100:
    A.Amount = int(fake.random_int())
    A.Creating_Date = fake.date()
    A.number_id = 2
    A.save()
    count += 1
'''
'''
for i in range(number1):
# Step 1 Insert data into User Sheet
    U.FullName = fake.name()
    U.Surname = fake.name()
    U.Address = fake.address()
    U.Age = fake.random_int(min=18, max=100)
    U.Company = fake.company()
    U.Status = fake.country()
    U.Creating_Date = fake.date()
    U.save()

for i in range(number2):
# Step 2 Insert data into Account Sheet
    A.Amount = int(fake.random_int())
    A.Creating_Date = fake.date()
    A.number_id = random.choice(fk)
    A.save()
'''

for i in range(100):
    # Step.1 Insert Fake data to Account Sheet
    A.Amount = int(fake.random_int())
    A.Creating_Date = fake.date()
    # Random pick PK in User Sheet

    A.number_id = random.randint(1, A.id)

    # Step.2 Insert Fake data to User Sheet
    U.FullName = fake.name()
    U.Surname = fake.name()
    U.address = fake.address()
    U.Age = fake.random_int(min=18, max=100)
    U.Company = fake.company()
    U.Status = fake.random_int()
    U.Creating_Date = fake.date()
    A.save()
    U.save()

