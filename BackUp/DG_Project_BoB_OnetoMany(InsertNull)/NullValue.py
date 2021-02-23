from BankData.models import Account, User
from faker import Faker
import random
import numpy as np

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
            user.fullname = str(np.NaN)
            user.surname = fake.first_name()
            user.address = str(np.NaN)
            user.age = str(np.NaN)
            user.company = str(np.NaN)
            user.status = str(np.NaN)
            user.creatingdate = str(np.NaN)
            user.save()
    def create_account(self):
        for i in range(self.number2):
            account = str(np.NaN)
            account.amount = str(np.NaN)
            account.creatingdate = str(np.NaN)
            account.account = str(np.NaN)
            account.A_account = User(id=(random.randint(1, self.number1)))
            account.save()

s1 = Fake_number(number1, number2)

