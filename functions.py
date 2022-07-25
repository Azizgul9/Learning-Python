#A function is block of code which only runs when it is called. In Python we do not use parantheses and curly brackets, we use indantation with tabs or space

#Create a function
# def sayHello(name):
#     print('Hello '+name)
# sayHello('Azizgul')

#Return value
def getSum(num1,num2):
    total = num1 + num2
    return total
print(getSum(5,9))

#A lyambda is a small anonyomous function.
#A lyambda function can take any number of arguments, but can only have one expression. Very similar to Js arrow function.
getNum = lambda num1,num2 : num1 + num2

print(getNum(2,9))

addOnetoNum = lambda num : num + 1

print(addOnetoNum(9))