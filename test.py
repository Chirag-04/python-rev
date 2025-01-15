#exception handling 
# we use exception handling in python to catch the errors / exception (like value error or ZeroDivisionError) int the code and provide user a better error message 

try:
    a = 12
    b = 2
    division =  a/b
    print('Value is : ' , division)
except ValueError:
    print('Enter the valid number')    
except ZeroDivisionError:
    print('Denominator cant be zero')


print('____________________________________________________');

my_list = [1,3,5,2,4,7,8,6,9]
l = my_list[2:5]
# start index , stop index (exclusive)  , step size 
print(l)


print('____________________________________________________');

def fibbo(n):
    if(n==0):
        return "invalid input"
    elif(n==1):
        return 0
    elif(n==2):
        return 1    
    return fibbo(n-1)+fibbo(n-2)

print(fibbo(10))

print('____________________________________________________');


#iterators are used to to iterate over data structure 
nums =[2,4,3,6,5,8,7,9]

it =  iter(nums)
print(next(it))

print('____________________________________________________')
# generators
# generator is a special function that returns an iterator
def func():
    yield 1
    yield 2
    yield 3


values =  func()
print(next(values))    
print(next(values))    
print(next(values)) 

print('____________________________________________________')

#classes and objects in python 

class Character:
    def __init__(self , health, damage , speed):
        self.health =  health
        self.damage = damage
        self.speed  = speed

    def double_the_speed(self):
        self.speed =  self.speed*2    


warrior =  Character(100 , 50 , 40)
print("health is : " , warrior.health)
print("damage is : " , warrior.damage)
print("speed is :" ,warrior.speed)  
warrior.double_the_speed()
print("new speed is :" ,warrior.speed)  


           