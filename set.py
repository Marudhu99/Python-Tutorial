# set - unordered,unique value,unchangeable
unique_item = {"ayyappan","mathiyalagan","sarathkumar","ayyappan",True,1} # True and 1 is considered the same value
print(unique_item)
print(type(unique_item))
# set constructor
set_value = set(("448","550","445"))
set_value2 = set(("443","448","222"))

# access item
for x in unique_item:
    print(x)

# add an item
set_value.add("679")

set_value.update(set_value2)
list_item = ["sarath","arul","kumaravel"]
set_value2.update(list_item)

# remove an item
set_value2.remove("sarath") # if the item to remove does not exist, remove() will raise an error
set_value2.discard("kumaravel") # if the item to remove does not exist, discard() will not raise an error
set_value2.pop() # remove a random item
set_value2.clear() # remove content only
del set_value2 # remove the set

# loop
for x in unique_item:
    print(x)

# join items
print("***************************************************")
item1 = {"23","chicken","mutton","egg"}
item2 = {"dosa","idly","egg"}
# item1.union(item2)
# item1.update(item2) # Both union() and update() will exclude any duplicate item

# keep only the duplicates
item1.intersection_update(item2)
print(item1)
item1.intersection(item2)
print(item1)

# keep all, but not the duplicates
item1.symmetric_difference(item2)
print(item1)
item1.symmetric_difference_update(item2)
print(item1)