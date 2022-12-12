# The __init__ method

# Dunders(magic methods)  __<name of dunder>__

class person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello my name is:",self.name)
p=person("Srikaran")
p.say_hi()



class A:
    def __init__(self):
        print(self)
        print("initialized")

    def __del__(self):
        print(self)
        print("I am dying")
a=A()



a=1
type(a)

a.__add__(5)



class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a+self.b+x
a=A()
print(a+3)