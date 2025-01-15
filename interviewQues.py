#1. Difference b/w list and tupple 
print("List are mutable while tuples are immutable , list are compartiely slower than tuples")

#2 What is decorator
print("Decorator is a function which takes another function as an argument , add some functionality then returns a function")

#3 what is module and package
# module can be considered as a file while package can be considered as a folder(directory)
#module is a single file with python code (.py)
#module has flat structure and package is hierarchical
# In order for a directory to be considered a Python package, it must contain an __init__.py file.


#4 is python a compiled lag
# python is primarily an interpreted language in which code is executed line by line rather than being compiled into machine code 


#5 Global, protected and public attributes in pythongloval
global_variable = "accessible throughout the program"
protected_variable = "marked with single underscore , still accessed and modified outside the class though it is not a good practice"
private_variable = "they are not accessible outside the class"

#6 how is exceptional handline done in python
# we use try except else finally(runs no matter what happen) 
# doubtful code / might raise exception like 100/0
#  we will put that in try block


#7 memory management in python 
# todo

# 8 which algo is used by python sort()
print("internally sort function uses Tim sort algorithm with worst case complexity of o(nlogn)  and its derived from merge sort and insertion sort")

#9 what is slicing in python 
print("used to extract a portion of string (substring)")

#10 is multithreading available in python and how
print("using the threading module mutilthreading is achievable in which muitple concurrent threads can be executed within same process")


#11 type conversion in python 
a = input('Enter the data')
print(a) 
# by default it takes string as an input 

# so we perform type conversion
# float() int() list() tuple()

li = [1,2,3,4,5]
def square(x):
    return x*x;
new_l = list(map(square , li))
print(new_l)

print("converting the existing type to desired type")

# 12 commonly used modules in python 
print("os , math , JSON , sys etc..")


#13 architecture of django 
print("django is a high level web framework build in python. It follows MVT architecture (model  views  template)")


