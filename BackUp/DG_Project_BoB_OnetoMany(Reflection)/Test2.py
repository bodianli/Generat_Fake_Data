from BankData.models import User
from faker import Faker
import random

fake = Faker()

amount = eval(input("How many data you want to generate? "))

class Create_user(object):
    dic = {'fullname': 'InsertName',
           'surname': 'InsertSurname',
           'address': 'InsertAddress',
           'age': 'InsertAge',
           'company': 'InsertCompany',
           'status': 'InsertStatus',
           'creating_date': 'InsertCreating_date'}

    def __init__(self, number):
        self.number = number

    def InsertName(self):
        user = User()
        user.fullname = fake.name()
        user.save()

    def InsertSurname(self):
        user = User()
        user.surname = fake.name()
        user.save()

    def InsertAddress(self):
        user = User()
        user.address = fake.address()
        user.save()

    def InsertAge(self):
        user = User()
        user.age = fake.random_int(min=18, max=100)
        user.save()

    def InsertCompany(self):
        user = User()
        user.company = fake.company()
        user.save()

    def InsertStatus(self):
        user = User()
        user.status = 'Active' if fake.random_int(min=0, max=1) == 1 else 'Deactive'
        user.save()

    def InsertCreating_date(self):
        user = User()
        user.creatingdate = fake.date()
        user.save()


# ret = getattr(Create_user, 'dic')
# print(ret)
insert1 = Create_user(amount)

for k in Create_user.dic:
    print(k)

key1 = input("Which two columns you want to insert: ")
x, y = key1.split(",")

func1 = getattr(insert1, Create_user.dic[x])
func2 = getattr(insert1, Create_user.dic[y])

func1()
func2()