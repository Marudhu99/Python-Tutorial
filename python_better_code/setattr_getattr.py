class Person():
    pass

person = Person()

person_info = {"firstName":"Marudhu","lastName":"Pandiyan"}
# The code is dynamically setting attributes on the `person` object using the `setattr()` function.
for key, value in person_info.items():
    setattr(person,key,value)

# The code is iterating over the keys of the `person_info` dictionary and using the `getattr()`
# function to retrieve the corresponding attribute value from the `person` object. It then prints the
# value of each attribute.
for key in person_info.keys():
    print(getattr(person,key))
