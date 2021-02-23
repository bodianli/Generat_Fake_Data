import json
from BankData.models import User    # Change(1)
from faker import Faker


# file_name = input("Json File: ")
# file = open(f"{file_name}.json", "w")

rows = eval((input('Generated row number: ')))
file = json.load(open('Test.json', 'r'))      # Change JSON to a dictionary
res = file['columns']      # Extract value of key --> return a list
file.close()
# print(list(res[0].values())[0])
# print(list(res[1].values())[0])
user = User()
fake = Faker()
column_list = []
for i in range(len(res)):
    column_list.append(list(res[i].values())[0])

# print(column_list)
# print(len(column_list))


full_name = None
sur_name = None
address = None
age = None
company = None
creatingdate = None

for k in range(rows):
    user = User()
    for i in range(len(column_list)):
        if column_list[i] == 'fullname':
            user.fullname = fake.name()
        if column_list[i] == 'surname':
            user.surname = fake.name()
        if column_list[i] == 'address':
            user.address = fake.address()
        if column_list[i] == 'age':
            user.age = fake.random_int(min=18, max=100)
        if column_list[i] == 'company':
            user.company = fake.company()
        if column_list[i] == 'creatingdate':
            user.creatingdate = fake.date()
    user.save()

print(f"Generate {rows} rows data for {file['table']} table")

# Not feasible
# for k in range(rows):
#     user = User()
#     for i in range(len(column_list)):
#         user.fullname = fake.name() if column_list[i] == 'fullname' else None
#         user.surname = fake.name() if column_list[i] == 'surname' else None
#         user.address = fake.address() if column_list[i] == 'address' else None
#         user.age = fake.random_int(min=18, max=100) if column_list[i] == 'age' else None
#         user.company = fake.company() if column_list[i] == 'company' else None
#         user.creatingdate = fake.date() if column_list[i] == 'creatingdate' else None
#     user.save()
