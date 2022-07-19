#A tuples is a collection which is ordered and changeable. Allows dublicate members
#Simple touple
fruit_tuple = ('Apples','bananas','orange')

#Using constructor
#fruit_tuple = tuple(('Apples','bananas','orange'))

#Get single value
#print(fruit_tuple[1])

#CAn not change value
#fruit_tuple[1] = 'grape'

#Touples with one value should have trailing comma
fruit_tuple_2 = ('apple',)

#Get length of tuple
#print(len(fruit_tuple_2)) 

del fruit_tuple_2



#A set is a collection which is unordered and unindexed. No dublicate members

#Create set
fruit_set = {'Apple','Orange','Grape',}

#check if in set
print('Apple' in fruit_set)

#Add to set
fruit_set.add('Grape')


#Remove
fruit_set.remove('Grape')

#Clear 
fruit_set.clear()

#Delete
del fruit_set
print(fruit_set)
