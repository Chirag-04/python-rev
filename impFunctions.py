# # # range 
# # def square(x):
# #     return x*x;

def cube(x): return x*x*x

l =  [1,2,3,4,5]
# # # return a list of squares of 

# # newl = []
# # for i in l:
# #     newl.append(square(i))

# # print(newl)   

# # newp = []
# # for i in l:
# #     newp.append(cube(i))
# # print(newp)    

newl = list(map(lambda x:x*x*x, l));
print(newl)

# def filter_function(a):
#     return a > 4

# p= [2,3,1,4,5,6,3,7,8,2]

# newl = list(filter(filter_function ,p));

# # print(newl)
# from functools import reduce

# number = [1,2,3,4,5]
#     #    [-13]

# def mySum(a , b):
#     return a-b

# sum = reduce(mySum , number)

# print(sum);


# lamda functions




