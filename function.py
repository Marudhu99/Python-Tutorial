# create a function using the def keyword
def my_function(name): # parameter
    print("it is the ",name)

# calling a function
my_function("method or function") # arguments

# Arbitrary Arguments, *args . receive a tuple of arguments
def sum(*numbers): #If you do not know how many arguments that will be passed into your function
    sum = numbers[0] + numbers[1]
    print(sum)

sum(1,2,3)

def child(kid1,kid2,kid3):
    print("Kid1:",kid1,"Kid2:",kid2)

child(kid1 = "bala", kid2 = "rajeshwari", kid3 = "rajesh")

# Arbitrary Keyword Arguments, **kwargs . receive a dictionary of arguments
def greet(**names):
    print("First name:",names["fname"],"Last name:",names["lname"])

greet(fname = "Marudhu" , lname = "Pandiyan")


# default parameter value
def countries(country = "india"):
    print("country:",country)

countries("switcherland")
countries()

# passing a list an value
food = ["parato","dosa","idly"]

def eat(food):
    for i in food:
        print(i)

eat(food)

# return values
def m1():
    return 5**2

print(m1())

# the pass statement
def m2():
    pass # some reason have a function definition with no content, put in the pass statement to avoid getting an error

