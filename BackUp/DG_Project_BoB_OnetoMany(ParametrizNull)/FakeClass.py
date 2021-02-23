from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

number1 = eval(input("How many Fake data you want for User?"))
number2 = eval(input("How many Fake data you want for Account?"))


# Create a class of "Fake"
# in this class, we have two attributes: number1 / number2
# in this class, we have two behaviour: Generate fake User / Generate fake Account
class Fake_number(object):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.create_user()
        self.create_account()
    def create_user(self):
        for i in range(self.number1):
            user = User()
            user.fullname = fake.name()
            user.surname = fake.name()
            user.address = fake.address()
            user.age = fake.random_int(min=18, max=100)
            user.company = fake.company()
            user.status = 'Active' if fake.random_int(min=0, max=1) == 1 else 'Deactive'
            user.creatingdate = fake.date()
            user.save()
    def create_account(self):
        for i in range(self.number2):
            account = Account()
            account.amount = int(fake.random_int())
            account.creatingdate = fake.date()
            account.account = fake.credit_card_number(card_type=None)
            account.A_account = User(id=(random.randint(1, self.number1)))
            account.save()

s1 = Fake_number(number1, number2)

