#A dictionary is a collection which is unordared, changeble and indexed.No dublicate members

#Simple dictionary
from cgi import print_exception


Person = {
    'frist_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#Using a constructor
# Person = dict(
#     frist_name = 'John',
#     last_name = 'Doe',
#     age = 30
# )

#Acces single value
# print(Person['frist_name'])
# print(Person.get('frist_name'))

#Add key/value
Person['phone'] = '0222-81-29-51'

#Get keys
#print(Person.keys())

#Get items
print(Person.items())
#print(Person)

person2 = Person.copy()
person2['city']= 'Boston'
#print(person2)

#Remove item
del(Person['age'])
Person.pop('phone')

#Clear
Person.clear()

#Get length
print(len(person2))
print(len(Person))

print(Person)
print(person2)

#List of dictionaries
people = [
    {'name': 'martha', 'age': 40},
    {'name': 'Bob', 'age': 26}
]
print(people[1]['name'])