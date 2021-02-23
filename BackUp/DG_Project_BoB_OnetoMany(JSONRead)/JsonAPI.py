

import json

'''
a = "python"             # Same as 'python'
b = {"name": "Python"}   # Same as {'name': 'Python'}
c = '{"name": "Python"}' # Json style String
'''



# Json write
# s = "json"
# json.dump(s, open('demo.txt', 'w'))
# s1 = ['info', {'name': "BOB", 'age': 23}]
# date = json.dumps(s1)
# print(date)


# Json read
file = json.load(open('Test.json', 'r'))
print(file)

# p2 = '["info", {"name": "BOB", "age": 23}]'
# json.loads(p2)
# print(p2)
# print(type(p2))

res = file['columns']
print(len(res))

for i in res:
    print("The column you create: ", i['name'])
    print("The type of data in this column: ", i['type'])
    print("The length or range of data type: ", i['range'])
    print("--------------------")

print(list(res[1].keys())[0])




# for i in range(len(res)):
#     column = res[i].key


# for i in res:
#     print(i)
#     print(i['name'])
#     print(i['type'])
#     print(i['range'])
#
# table = input("Which table you want to insert: ")