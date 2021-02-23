from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

# number1 = 10  Number of User
# eval(input("How many Fake data you want for User?"))
# number2 = 100  eval(input("How many Fake data you want for Account?"))

# fk = [i for i in range(number1)]

user = User()
user.Fullname = fake.name()
user.Surname = fake.name()
user.Address = fake.address()
user.Age = fake.random_int(min=18, max=100)
user.Company = fake.company()
user.Status = fake.country()
user.Creating_Date = fake.date()
user.U_account = fake.credit_card_number(card_type=None)
user.save()

# Step.2 Insert Fake data to Account Sheet
account = Account()
account.A_Amount = int(fake.random_int())
account.A_Creating_Date = fake.date()
account.save()
