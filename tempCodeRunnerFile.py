#exception handling 
# we use exception handling in python to catch the errors / exception int the code and provide user a better error message 

a = int(input('Enter first number'))
b = int(input('Enter second number'))
try:
    division =  a/b
    print('Value is : ' , division)
except ZeroDivisionError:
    print('Denominator cant be zero')

