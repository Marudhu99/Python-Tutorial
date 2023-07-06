# lambda function is a small anonymous function
x =  lambda a : a + 2
print(x(3))

y =  lambda a,b : a + b
print(y(4,3))

def my_func(n):
    return lambda x : x + n

number = my_func(3)
print(number(5)) # for lambda inside the my_func method