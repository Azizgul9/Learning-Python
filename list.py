#A list is a collection which is ordered and changeable. Allows dublicate members

#Create list
# numbers = [1,2,3,4,5]
# print(numbers)

#Using a constructor
numbers= list((1,2,3,4,5))
fruits=['Apples','Oranges','Pears']

#Get value
print(fruits[2])

#Get len
print(len(fruits))

#Appent to list
fruits.append('watermelon')


#REmove from list
fruits.remove('Apples')

#Insert into position
fruits.insert(2,'strawberries')

#Remove from certain position
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Reverse sort
fruits.sort(reverse = True)

print(fruits)



