#decorator
#suppose in the division function we want to maintain a functinality in which numerator will always be greater than denominator (a >b)
# but lets say this piece of code is written in lot of other files 
# so it is not feasile to change it 
# so through decorator we can change the functionality without changing the original function definition
# decorators are the function that accepts function as an argument and returns function too
def div(a,b):
    print(a/b)
    
def decorate(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner

new_f = decorate(div) 

new_f(2,4)