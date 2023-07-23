names = ["Marudhu","Arul","Sarath"]

index = 0
for name in names:
    print(index,name)
    index += 1

# The code `for index,name in enumerate(names,start=1):` is using the `enumerate()` function to
# iterate over the `names` list and retrieve both the index and the value of each element.
for index,name in enumerate(names, start=1):
    print(index,name)