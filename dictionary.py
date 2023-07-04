# dict - ordered, changeable, not allowed duplicate
information = {
    "name" : "Marudhu",
    "age" : 23,
    "isMarried" : False
}

print(information)
print(type(information))
print(len(information))

# dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# access items
print(information["age"])
print(information.get("name"))
print(information.keys())
print(information.values())
print(information.items())
information["age"] = 24 # change value
print(information.values())

# update items
information.update({"name" : "Marudhu Pandiyan"})
print(information)

# add items
information["gender"] = "Male"
information.update({"hobbies" : ["cricket","workout","coding"]})

print(information)

# removing items
information.pop("gender")
print(information)
information.popitem() # remove the last item
print(information)
del information["age"]
print(information)
information.clear() # content removed
print(information)
del information # completely delete the dict
# print(information) 


information = {
    "name" : "Marudhu",
    "age" : 23,
    "isMarried" : False
}
# loop
for x in information:
    print(x)

for x in information.keys():
    print("Keys:",x)

for x in information.values():
    print("Values:",x)

for x,y in information.items():
    print(x,y)

# copy a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
mydict = dict(thisdict)
print(mydict)

# nested dictionaries
myfamily = {
    'child1' : {'name': 'Emil', 'birthYear': 2000},
    'child2' : {'name': 'Tobias','birthYear': 2003},
    'child3' : {'name' : 'Arul', 'birthYear': 2004}
}
print(myfamily)

brother1 = {"name" : "Marudhu","age": 23}
brother2 = {"name" : "Arul","age": 21}
brother3 = {"name" : "Sarath","age": 20}

mySibilings = {
    'brother1' : brother1,
    'brother2' : brother2,
    'brother3' : brother3
}
print(mySibilings)

# accessing items in nested dictionary
print(mySibilings["brother2"]["name"])