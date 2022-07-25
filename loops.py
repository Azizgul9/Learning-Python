#A for loop is used for itering over sequence(that is either a lis, a tuple, a dictionary, a set,or a string).
#simple for loop
people = ['John', 'Jannet','Kril']

#beak out


# for person in people:
#     print('Current person is', person)
#     if person == 'Jannet':
#         break

#Continue

# for person in people:
#     if person == 'Jannet':
#         continue
#     print('Current person is', person)

#Range 

# for i in range(len(people)):
#     print('Current people: ', people[i])

# for i in range(0,10):
#     print(i)

#While loop execute a set of statement as lon as condition is true 
count = 0 
while count <= 10:
    print('count ',count)
    count += 1