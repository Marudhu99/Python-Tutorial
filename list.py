list1 = ["abc", 34, True, 40, "male"]
print("Length:",len(list1)) # length of list1

#List constructor
list2 = list(("cat","rat","tiger","camel","rat")) #allow duplicates
print(type(list2))

#Access Items
print(list2[1]) 
print(list2[1:3])
print(list2[:5])
print(list2[2:])
print(list2[-3:-1]) #range of negative index

#check if item exist
if "abc" in list1:
    print("list1 has abc text")

#change item values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
#change a range of item values
thislist[1:3] = ["grabes","jackfruit"]
print(thislist)

#insert the item without replacing any of the existing values
thislist.insert(1,"orange")
print(thislist)

# add item value
thislist.append("strawberry")
print(thislist)

#extend list
fruits1= ["kiwi","pineapple","papaya"]
fruits2 = ["pomegranate","watermelon","lemon"]
fruits1.extend(fruits2)
print(fruits1)

# remove item value
fruits1.remove("kiwi")

# remove specified index
fruits1.pop(2)

# remove specified index also using del
del fruits2[2]
print(fruits2)

kids_name = ["bala","pugi","vaji"]
del kids_name # deleted kids_name list
# print(kids_name) 

kids_name = ["bala","pugi","vaji"]
kids_name.clear() # remove content only
print(kids_name)

# loop list
numbers = [1,2,5,23]
for number in numbers :
    print(number)

# loop through the
for i in range(len(numbers)):
    print(numbers[i])

# using a while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "apple" in x:
        newList.append(x)

print(newList)

# With list comprehension
# new_list = [expression for item in iterable if condition]
newList2 = [x for x in fruits if "banana" in x]
print(newList2)

# sort list
nums=[4,67,-89,23,12]
nums.sort()
print("Sorted List:", nums)

# reverse using sort list
nums.sort(reverse = True)
print("Reverse list:",nums)

# using reverse method
nums.reverse()
print(nums)

# copy list
my_list= ['a', 'b']
copy_of_list = my_list[:] #using slicing to create shallow copies of lists
copy_of_list2 = my_list.copy()
copy_of_list3 = list(my_list)

# join two list
l1 = ['a','b','c']
l2 = ['d','e','f']
joined_lists = l1 + l2
print(joined_lists)

for x in l2:
    l1.append(l2)

l1.extend(l2)

