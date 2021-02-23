from BankData.models import User
from faker import Faker
import random

fake = Faker()


class Create_user(object):
    dic = {'fullname': 'InsertName',
           'surname': 'InsertSurname',
           'address': 'InsertAddress',
           'age': 'InsertAge',
           'company': 'InsertCompany',
           'status': 'InsertStatus',
           'creating_date': 'InsertCreating_date'}

    def InsertName(self):
        user.fullname = fake.name()
        user.save()
    def InsertSurname(self):
        user.surname = fake.name()
        user.save()
    def InsertAddress(self):
        user.address = fake.address()
        user.save()
    def InsertAge(self):
        user.age = fake.random_int(min=18, max=100)
        user.save()
    def InsertCompany(self):
        user.company = fake.company()
        user.save()
    def InsertStatus(self):
        user.status = 'Active' if fake.random_int(min=0, max=1) == 1 else 'Deactive'
        user.save()
    def InsertCreating_date(self):
        user.creatingdate = fake.date()
        user.save()

for k in Create_user.dic:
    print(k)

amount = eval(input("How many data you want to generate? "))
key1 = input("Which two columns you want to insert: ")
x, y, z = key1.split(",")


for i in range(amount):
    user = User()
    insert = Create_user()
    insert_1 = getattr(insert, Create_user.dic[x])()
    insert_2 = getattr(insert, Create_user.dic[y])()
    insert_3 = getattr(insert, Create_user.dic[y])()