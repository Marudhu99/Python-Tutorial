'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 50
b = 100

if a < b:
    print("b greater than a")
elif a > b:
    print("a greater than b")
else:
    print("a & b both are equal")

age = 18
gender = "male"

if age >= 18 or gender == "male" :
    print("you are eligible")

gender = "female"
if age == 18 and gender == "female":
    print("you are not eligible ")

if not age < 18:
    print("above 18")

# Short Hand If ... Else
# value_if_true if condition else value_if_false
print("I am marudhu") if age > 18 else print("I am sarath") 

# nested if
num = 20
if num > 10:
    if num >= 20:
        print("it is the biggest number")
    else:
        print("it is a smallest number")




