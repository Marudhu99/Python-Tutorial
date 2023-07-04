'''
text type : str
numeric type : int,float,complex
sequence type : list,tuple,range
mapping type : dict
set type : set,frozenset
boolean type : bool
binary type : bytes,bytearray,memoryview
none type : NoneType
'''

x = "Hello world!" #str
print(type(x))

y = 5 #int
print(type(y))

z = 3.14 #float
print(z)

a = 1j #complex
print(type(a))

family = ["arul","sarathkumar","ishwarya"] #list
print(type(family))

fruits = ("mangao","grapes","orange","apple") #tuple
print(type(fruits))

_range = range(6) #range
print(_range)
print(type(_range))

_map = {"name":"Marudhu","age":23} #dict
print(type(_map))

_set = {"stalin","karunanithi","jeyalalitha"} #set
print(type(_set))

_frozenSet = frozenset({"stalin","karunanithi","jeyalalitha"})
print(type(_frozenSet))

isMarried = True #bool
print(type(isMarried))

_byte = b"Hello" #bytes
print(type(_byte))

_byteArray = bytearray(6) #bytearray
print(type(_byteArray))

_memoryview = memoryview(bytes(5)) #memoryview
print(type(_memoryview))

e = None #NoneType
print(type(e))
