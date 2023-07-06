# while loop
i = 1
while i <= 10:
    print(i)
    if i == 5:
        print("break")
        break # we can stop the loop even if condition true
    i += 1

print("**********************************")

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("we can stop the current iteration")
        continue
    print(i)

# for loop
list1 = ["marudhu","jayaraj","ayyappan"]
for x in list1:
    print(x)

for i in range(len(list1)):
    print(list1[i])

for i in list1:
    if i == "jayaraj":
        break
    print(i)


for i in list1:
    if i == "jayaraj":
        continue
    print(i)

# else in for loop
for i in range(6):
    print(i)
else:
    print("task completed")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
# nested loop
for x in adj:
    for y in fruits:
        print(x,y)

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0,1,2]:
    pass 