# open function takes two parameter : filename, mode - r:read,a:append,w:write,x-create
import os

f = open("demo_file.txt","r")
print(f.read())
print(f.read(5)) #you can also specify how many characters you want to return
print(f.readline()) # read only one line
# f.close() # It is a good practice to always close the file when you are done with it.

#write
f = open("demo_file.txt","a")
f.write("I had been working as a junior developer for 6 months")
print(f.read())
f.close()

#create
newFile = open("newFile.txt","x")

#write
newFile = open("newFile.txt","w")
newFile.write("new file created")

#del
if os.path.exists("newFile.txt"):
    os.remove("newFile.tx")
else:
    print("The file does not exist")