from one_to_more.models import User_more
from one_to_more.models import Account_more
from faker import Faker
import sys
fake = Faker()
import random
import time

class GenerateFakeData():
    def __init__(self):
        self.user_num = int(input("Please insert a number to generate fake data for User table: "))
        print(f'Null status check for User table:\nInsert 0 means insert null\nInsert 1 means insert fake data\n')
        self.check_User_Name = int(input('Null check for Name: ')) # User table setting
        self.check_User_Surname = int(input('Null check for Surname: '))
        self.check_User_Address = int(input('Null check for Address: '))
        self.check_User_Age = int(input('Null check for Age: '))
        self.check_User_Company = int(input('Null check for Company: '))
        self.check_User_Status = int(input('Null check for Status: '))
        self.check_User_Creating_Date = int(input('Null check for Creating_Date: '))
        print('You have completed the User table setting')
        self.account_num = int(input("\nPlease insert a number to generate fake data for Account table: "))
        print(f'\nFake Data generation task starts.')
        self.start_time = time.perf_counter() # starts time
        self.num_rows_generate_User()  # generate rows for User table
        self.total_users = int(User_more.objects.count())  # Check the max User ID
        self.num_rows_generate_Account() # generate rows for Account table
        self.end_time = time.perf_counter() # end time
        self.time_check() # calculate total running time
    def num_rows_generate_User(self):
        for i in range(self.user_num):  # Generate n rows of fake data for User table
            # insert fake data to User table
            if self.check_User_Name == 0:
                User_Name = None
            else:
                User_Name = fake.name()
            if self.check_User_Surname == 0:
                User_Surname = None
            else:
                User_Surname = fake.name()
            if self.check_User_Address == 0:
                User_Address = None
            else:
                User_Address = fake.address()
            if self.check_User_Age == 0:
                User_Age = None
            else:
                User_Age = fake.random_int(min=16, max=110)
            if self.check_User_Company == 0:
                User_Company = None
            else:
                User_Company = fake.company()
            if self.check_User_Status == 0:
                User_Status = None
            else:
                Statu = fake.random_int(min=0, max=1)
                if Statu == 1:  # Confirm Status is Active or Deactive
                    User_Status = 'Active'
                else:
                    User_Status = 'Deactive'
            if self.check_User_Creating_Date == 0:
                User_Creating_Date = None
            else:
                User_Creating_Date = fake.date()
            User_Fake_Data = User_more(Name=User_Name, Surname=User_Surname, Address=User_Address, Age=User_Age,
                                       Company=User_Company, Status=User_Status, Creating_Date=User_Creating_Date)
            User_Fake_Data.save()
        print(f'\nYou have generated {self.user_num} rows for User tables')
    def num_rows_generate_Account(self):
        #if self.account_num == self.total_users:
         #   print(f"\nError message:\nThe max user id is {self.total_users}.\n"
          #        f"If you insert an account generate number is over the max user id {self.total_users},you will get this error."
          #        f"\nYou have generated 0 row of data for Account table.")
       # else:
        for i in range(self.account_num):  # Generate n rows of fake data for Account table
                # insert fake data to Account table
            Account_Amount = int(fake.random_int())
            Account_Creation_Date = fake.date()
            Fake_Account_ID = fake.bban()
            Fake_User_ID = User_more(id=(random.randint(1, self.total_users)))
            Account_Fake_Data = Account_more(Amount=Account_Amount, Creation_Date=Account_Creation_Date,
                                                 Account_ID=Fake_Account_ID, User_ID=Fake_User_ID)
            Account_Fake_Data.save()
        print(f'\nYou have generated {self.account_num} rows for Account')
    def time_check(self): # calculate total running time
        total_time = self.end_time-self.start_time
        mins = total_time // 60
        seconds = total_time % 60
        print(f"\nFake data generation task is done."
              f"\nThe task took {mins:.0f} minutes {seconds:.0f} seconds.")
    #def null_check(self):
    #     check_User_Surname = int(input('check: '))
    #     return check_User_Surname

#num_user = int(input("Please insert a number to generate fake data for User table: "))
#num_account = int(input("\nPlease insert a number to generate fake data for Account table: "))

Generate_Fake_Data = GenerateFakeData()
