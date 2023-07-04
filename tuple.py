# tuple - it is defined order cannot change
thistuple = ("apple", "banana", "cherry","apple") # allow duplicates
print(thistuple)
print(type(thistuple))
print(len(thistuple))

tuple1 = ("mango",) # Create tuple with one item
#NOT a tuple
tuple_not = ("apple")
print(type(thistuple))

# tuple constructor
tuple2 = tuple(("flowers","vechicles"))

# get the tuple
print(tuple2[1])
print(tuple2[:1])
print(tuple2[1:])
print(tuple2[-1:])

# unchangeable or immutable
change_list = list(tuple2) # convert to list and then we can edit
change_list[1] = "kiwi"
change_list.append("orange")
change_list.insert(2,"watermelon")
change_list.remove("watermelon") 
tuple2 = tuple(change_list)
print("Tuple after changing: ", tuple2)

del tuple2 # del keyword can delete the tuple completely

# unpack tuples
name1 = ("Marudhu","Arul","Sarath") # pack tuples
(marudhu,arul,sarath) = name1 # unpack tuples
print(marudhu)
print(arul)
print(sarath)

# using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # ['cherry', 'strawberry', 'raspberry']

for x in fruits:
    print(x)

for x in range(len(fruits)):
    print(fruits[x])

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# join tuple
join_tuple = tuple1 + tuple2
print(join_tuple)

# multiply tuple
multiply_touple = tuple1 * 2
print(multiply_touple)

numbers = (2,4,5,2,7,7,8)
numbers.index(4)