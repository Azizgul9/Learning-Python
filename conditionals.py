#If/else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

#Comparison operators (==, !=, >, <, >=, <=) - Used to compare values
#Simple if
# if x == y :
#     print(f'{x} is equal to {y}')
#Id/else
# if x>y :
#     print(f'{x} is greater than {y}')
# else :
#     print(f'{x} is lessen than {y}')   
#elif
# if x>y :
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{x} is lessen than {y}')   

#Nested if

# if x>2 :
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than 10')

#Logical operators (and, or, not) - Used to combine conditional statements
#and
# if x> 2 and x<=10:
#      print(f'{x} is greater than 2 and less than 10')
#or
# if x> 2 or x<=10:
#     print(f'{x} is greater than 2 or less than 10')   
#not 
# if not(x == y):
#     print(f'{x} is not equal to {y}')      

#Membership operators (not, not in) - Membership operators are used to test if a sequence is presented in a sequence
numbers = [1, 2, 3, 4, 5, 6]

#in
# if x in numbers:
#     print(x in numbers)

#not in

# if x not in numbers:
#     print(x not in numbers)

#Identity operators (is, is not) - Compare the objects, not if they are equal
# #is 
# if x is y:
#     print(x is y)

#is not 
if x is not y:
    print(x is not y)
