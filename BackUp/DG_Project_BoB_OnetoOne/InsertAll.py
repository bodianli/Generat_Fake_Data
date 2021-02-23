from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

number1 = eval(input("How many Fake data you want for User?"))
# number2 = 100  eval(input("How many Fake data you want for Account?"))

# fk = [i for i in range(number1)]

for i in range(number1):
    # Step.1 Insert User Data with User's Account Number
    user = User()
    user.fullname = fake.name()
    user.surname = fake.name()
    user.address = fake.address()
    user.age = fake.random_int(min=18, max=100)
    user.company = fake.company()
    user.status = fake.country()
    user.creatingdate = fake.date()
    user.save()
    # Step.2 Insert Fake data to Account Sheet
    account = Account()
    account.amount = int(fake.random_int())
    account.creatingdate = fake.date()
    account.account = fake.credit_card_number(card_type=None)
    account.save()

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
    U.account = A
    # A.save()
    U.save()  #
'''