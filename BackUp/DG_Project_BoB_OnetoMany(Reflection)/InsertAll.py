from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

user = 10  # Number of User
# eval(input("How many Fake data you want for User?"))
account = 100

## fk = [i for i in range(number1)]
## fk

class Fake(object):


    def Generate_User(n):
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


    def Generate_Account(n):
        for i in range(n):
            account = Account()
            account.amount = int(fake.random_int())
            account.creatingdate = fake.date()
            account.account = fake.credit_card_number(card_type=None)
            account.A_account = User(id=(random.randint(1, n)))
            account.save()


Insert_User = Generate_User(number1)
Insert_Account = Generate_Account(number2)
