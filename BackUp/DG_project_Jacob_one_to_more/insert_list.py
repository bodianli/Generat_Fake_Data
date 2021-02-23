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
        print(f'Null status check for User table:'
              f'\nPlease select columns to insert fake data. The columns were not select will use Null value instead'
              f'\nColumn list: Name,Surname,Address,Age,Company,Status,Creating_Date\n')
        self.check_User_table = str(input('Please select columns: '))  # Chose which columns you want to feed fake data
        #self.User_table_list = self.check_User_table.split(",") # Split columns you chose into a list
        self.check_User_Name = 'Name'
        self.check_User_Surname = 'Surname'
        self.check_User_Address = 'Address'
        self.check_User_Age = 'Age'
        self.check_User_Company = 'Company'
        self.check_User_Status = 'Status'
        self.check_User_Creating_Date = 'Creating_Date'
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
            # Check which column you want to insert fake data
            if self.check_User_Name in self.check_User_table:
                User_Name = fake.name()
            else:
                User_Name = None
            if self.check_User_Surname in self.check_User_table:
                User_Surname = fake.name()
            else:
                User_Surname = None
            if self.check_User_Address in self.check_User_table:
                User_Address = fake.address()
            else:
                User_Address = None
            if self.check_User_Age in self.check_User_table:
                User_Age = fake.random_int(min=16, max=110)
            else:
                User_Age = None
            if self.check_User_Company in self.check_User_table:
                User_Company = fake.company()
            else:
                User_Company = None
            if self.check_User_Status in self.check_User_table:
                Statu = fake.random_int(min=0, max=1)
                if Statu == 1:  # Confirm Status is Active or Deactive
                    User_Status = 'Active'
                else:
                    User_Status = 'Deactive'
            else:
                User_Status = None
            if self.check_User_Creating_Date in self.check_User_table:
                    User_Creating_Date = fake.date()
            else:
                User_Creating_Date = None
            User_Fake_Data = User_more(Name=User_Name, Surname=User_Surname, Address=User_Address, Age=User_Age,
                                       Company=User_Company, Status=User_Status, Creating_Date=User_Creating_Date)
            User_Fake_Data.save()  # Save new insert data
        print(f'\nYou have generated {self.user_num} rows for User tables')
    def num_rows_generate_Account(self):
        for i in range(self.account_num): # Generate n rows of fake data for Account table
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


Generate_Fake_Data = GenerateFakeData()
