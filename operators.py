#Arithmetic operator
a = 5
b = 4

addition = a+b
substraction = a-b
multiplication = a*b
division = a/b
modulus = a%b
exponentiation = a**b # 5*5*5*5
floor_division = a//b # rounds the result down to the nearest whole number

print("Addition:",addition)
print("Substraction:",substraction)
print("Multiplicaiton:",multiplication)
print("Division",division)
print("Modulus:",modulus)
print("Exponentiation:",exponentiation)
print("Floor_division:",floor_division)

#Assignment operator
x = 5
x += 5 # x = x + 3
x -= 2 # x = x - 3
x *= 3 # x = x * 3
x /= 2 # x = x / 3
x %= 2 # x = x % 3
x //= 4 # x = x // 3
x **= 3 # x = x ** 3

#Comparator operator
x == 5
x != 5
x > 4
x < 6
x >= 5
x <= 6

#Logical operator
# (and, or and not )
x > 4 and x >= 5 #and
x < 5 or x == 5 #or
not(x < 5 or x == 5) #not

#Identity operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is not y) # returns True because x is not the same object as y

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#Membership operator
animals = ["cat","dog","lion"]
print("lion" in animals) # True
print("cat" is not animals) # False

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers

# Operator Precedence
d = (3+2)-(34+2)
print(d) #Parentheses has the highest precedence