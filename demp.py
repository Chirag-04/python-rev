# print("hi");

# name= "chirag"
# print("my name is " , name)

# # name=  input('Enter you name')
# print("your name is " , name)

# by default this input function is used to tae string/characters as an input 

# n = int(input('Enter you fav number '))
# print("your fav number is : " , n)

#* range 
# for i in range(0, 10, 1):
#     print(i)

# for i in range(0 , 10 , 2):
#     print(i)

# 0 2 4 6 8 

#* #=> single line commment and '''comment''' for multi-line comments

#* new line character
# print("\n") 
# print("\\")
# print('\t') #tab space


#* Slicing string[start_index :end_index :  step_value]
# start_index is inclusive and end_index is exclusive
# para = "abcdefghijklmnopqrstuvwxyz"
# s = para[4:9:2]
# print(s);


#* String methods
# para = "chirag04NSUT"
# isalnum()
# isalpha()
# isdigit()
# islower()
# isupper()


#*list data structure 
# list is ordered, indexed , mutable
# can also store hetro data
# my_list = [1 , 2.3 , "Chirag" , False]
# print(my_list)
# sports = ['cricket' , 'football' ,'cricket' ,'basketball', 'cricket' ]
# print(sports)
# print(sports[1])
# sports.insert(3,'baseball')
# print(sports)
# sports.pop(3)
# print(sports)
# sports.append('golf')
# sports.append('hockey')
# print(sports)
# sports.insert(2,'rugby')
# print(sports)
# sports.reverse()
# print(sports)
# # sports.sort(reverse=True)
# # print("count is  :"  ,sports.count("cricket"))

# lucky_number = [11,4,6,2,7,9,8]
# print(lucky_number)
# lucky_number.sort(reverse=True) #increasing order
# print(lucky_number)

#* tuple data structure 
# data strcture used to store data
# Tuples are ordered,indexing,immutable and most secured collection of elements

# my_tuple = (1 , 2.3 , "chirag" ,True, "chirag")
# your_tuple= ("usa" , 3.4444)
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[3])
# print(my_tuple[-1])
# print(my_tuple[1:])

# print(2*my_tuple)
# new_tuple = my_tuple + your_tuple
# print(new_tuple)

# print(my_tuple.count('chirag'))


#*sets
# data strcture to store unique data
# add remove pop issubet
# unordered 
# my_set = {1,2.3,"chirag", True}
# my_set.add(45)
# print(my_set);
# my_set.pop();
# print(my_set);
# # my_set.clear();
# # print(my_set);
# s1 = {1,3,5,7,9,10}
# s2 = {2,4,6,7,8,9,10}
# s = s1.intersection(s2)
# print(s);
# s3 = s1.union(s2)
# print(s3)

# # issubset()

#* Dictionary : a ds which is used to store data in key-value format (for every data entry threre will be key and a value corresponding to that )
