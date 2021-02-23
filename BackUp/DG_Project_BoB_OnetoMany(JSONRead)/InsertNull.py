from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

print(f'\nwhich columns you want to insert fake data?\n'
      f'fullname : 1\n'
      f'surname : 2\n'
      f'address : 3\n'
      f'age : 4\n'
      f'company : 5\n'
      f'status : 6\n'
      f'creatingdate : 7\n'
      f'amount : 8\n'
      f'account number : 9\n')

n1, n2 = eval(input("Enter the column you want to insert separated by commas: "))

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
            user.fullname = fake.name() if (n1 == 1 or n2 == 1) else None
            user.surname = fake.name() if (n1 == 2 or n2 == 2) else None
            user.address = fake.address() if (n1 == 3 or n2 == 3) else None
            user.age = fake.random_int(min=18, max=100) if (n1 == 4 or n2 == 4) else None
            user.company = fake.company() if (n1 == 5 or n2 == 5) else None
            if n1 == 6 or n2 == 6:
                status = fake.random_int(min=0, max=1)
                if status == 1:
                    user.status = 'Active'
                else:
                    user.status = 'Deactive'
            else:
                user.status = None
            user.creatingdate = fake.date() if (n1 == 7 or n2 == 7) else None
            user.save()
        print(f'\nYou have generated {self.number1} rows for User tables successfully')
    def create_account(self):
        for i in range(self.number2):
            account = Account()
            account.amount = int(fake.random_int()) if (n1 == 8 or n2 == 8) else None
            account.creatingdate = fake.date() if (n1 == 7 or n2 == 7) else None
            account.account = fake.credit_card_number(card_type=None) if (n1 == 9 or n2 == 9) else None
            account.A_account = User(id=(random.randint(1, self.number1)))
            account.save()
        print(f'\nYou have generated {self.number2} rows for Account tables successfully')


s1 = Fake_number(number1, number2)