def my_func():
    x = 10 # local variable
    print(x)

my_func()

# function inside function
def method1():
    def innerMethod2():
        print("inner method")
    innerMethod2()

method1()

# global scope 
global_variable = 500

# naming variable
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# global keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)