from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()
A = Account()
U = User()

U.FullName = fake.name()
U.Surname = fake.name()
U.Address = fake.address()
U.Age = fake.random_int(min=18, max=100)
U.Company = fake.company()
U.Status = fake.country()
U.Creating_Date = fake.date()
U.save()
