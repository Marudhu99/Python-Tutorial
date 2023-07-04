x = "Hello"
print(type(x))

# multiline strings using three double quotes or single quotes
a = """Marudhu is a junior devloper for 6 months.
    and I have been working as a support analyst at Virsec team."""
print(a)

# strings are array. python does not have a character datatype
sentence = "I checking on it"
print("String are array",sentence[3])

# looping through a string
for x in "banana":
    print(x)

# length of string
word = "Everything is good"
print(len(word))

# check string and using if
print("is" in word) # output:boolean type

if "good" in word:
    print("good txt present in word")

if "Everything" not in word:
    print("Everything txt is not there in word")


# slicing strings
print("****************************************")
txt = "How are you?"
print(txt[2:len(txt)])
print(txt[:5]) #slice from the start
print(txt[1:]) #slice to the end
print(txt[-3:-1]) #negative indexing

# modifying strings
print("****************************************")
text = " Python,Java "
print(text.upper()) # upper case
print(text.lower()) # lower case
print(text.strip()) # remove whitespace left and back
print(text.lstrip()) # remove left whitespace
print(text.rstrip()) # remove right whitespace
print(text.replace(" ","_"))
text = text.split(",")
print(text)
print(type(text))

# string concatenation
print("****************************************")
fname = "Marudhu"
lname = "Pandiyan"
fullname = fname + lname
print("fullname:",fullname)
print("fullname",fname+" "+lname)

# string format
print("**************String format**************************")
age = 23
count = 5
text = "My name is MarudhuPandiyan. I am {} years old. I bought {} cars." #index numbers {0}
print(text.format(age,count)) 

# escape character
print("***************Escape character*************************")
string = "I am from \"chennai\".\nI did my graduation bsc chemistry.It\'s alright.\rI had been working as a \tjunior developer"
print(string)

# string methods
print("*****************String Methods**************************")
name = "marudhu pandiyan"
print(name.capitalize())

words = ["Hello", "World!"]
joined_string = " ".join(words)  # joined_string = "Hello World!"
print(joined_string)

my_string = "Hello, World!"
index1 = my_string.find("World")  # index1 = 7
index2 = my_string.index("World")  # index2 = 7

my_string = "Hello, World!"
starts_with_hello = my_string.startswith("Hello,")
print(starts_with_hello) #True
ends_with_world = my_string.endswith("world")
print(ends_with_world) #False

num_string = "12345"
print(num_string.isdigit())
alpha_string = "Hello"
print(alpha_string.isalpha)
alphanumeric_string = "Hello"
print(alphanumeric_string.isalnum)