list = ["Bat","Ball","Stump"]
it = iter(list)

print(next(it))
print(next(it))
print(next(it))

for x in list:
    print(x)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1
        return x
    
myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
    
