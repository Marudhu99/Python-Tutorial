# create a class
class MyClass:
    x = 5

# create a object
obj = MyClass()
print(obj.x)

class Person:
    def __init__(self,name,age): # like a constructor
        self.name = name
        self.age = age

    def __str__(self): # like toString
        return f"{self.name}({self.age})"

obj1 = Person("Marudhu",23)
print(obj1.name)
print(obj1.age)
print(obj1)

# modify object properties
obj1.name = "MarudhuPandiyan"

# delete object properties
del obj1.age


