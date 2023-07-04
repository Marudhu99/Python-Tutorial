x = 4
print(type(x)) # x is of type int
x = "Marudhu" # x is now of type str
print(type(x))

#camel case
myVariableName = "John"

#pascal
MyVariableName = "Marudhu"

#snake case
my_variable_name = "Arul"

#many values to multiple variables
x,y,z = "orange","mango","grapes"
print(x)
print(y)
print(z)

#one value to multiple variables
a = b = z = "Kumaravel"

#unpack a collection
print("*************************************")
friends = ["Kumaravel","Paruthi","Mugunthan","Balamurugan"]
k,p,m,b = friends

print(k)
print(p)
print(m)
print(b)


global_variable = 5

def myFunc():
    localVariable = 6
    print("localVariable :",localVariable)
    return localVariable

print(myFunc())


