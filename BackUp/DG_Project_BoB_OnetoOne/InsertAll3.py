from BankData.models import Account, User
from faker import Faker
import random

fake = Faker()

number1 = 10  # Number of User
# eval(input("How many Fake data you want for User?"))
# number2 = 100  eval(input("How many Fake data you want for Account?"))

# fk = [i for i in range(number1)]

for i in range(number1):

    # For User Data
    Fullname_U = fake.name()
    Surname_U = fake.name()
    Address_U = fake.address()
    Age_U = fake.random_int(min=18, max=100)
    Company_U = fake.company()
    Status_U = fake.country()
    Creating_Date_U = fake.date()
    account_U = fake.credit_card_number(card_type=None)

    # For Account Data
    Amount_A = int(fake.random_int())
    Creating_Date_A = fake.date()
    account_A = UDATA

    UDATA = User.objects.create(Fullname=Fullname_U,
                                Surname=Surname_U,
                                Address=Address_U,
                                Age=Age_U,
                                Company=Company_U,
                                Status=Status_U,
                                Creating_Date=Creating_Date_U,
                                U_account=account_U)

    ADATA = Account.objects.create(A_Amount=Amount_A,
                                   A_Creating_Date=Creating_Date_A,
                                   A_account=account_A)
    UDATA.save()
    ADATA.save()
