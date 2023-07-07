import mymodule
# import mymodule as mod => rename a module
import platform # predefined module
from mymodule import person # import the only person

mymodule.greeting()
print(mymodule.person["name"]) # variable in module

print(platform.system())
print(dir(platform)) # here is a built-in function to list all the function names (or variable names) in a module