print(1,2,3,4,5,sep=",")


def hello():
    print("Hello World !")
    return 1
a=1
a=hello
a()


def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)
func(c=1,a=2,b=3)

# Arguments in python

# Required arguments
# Default arguments
# Optional positional only arguments
# Required keyworded only arguments
# Default keyworded only arguments
# Optional keyworded only arguments


# Required arguments
def func (a,b):
    print(a,b)
func(1,2)


# Default arguments
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)


# Optional positional arguments
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,"Rajiv",1.5)


#  Required keyworded only arguments
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)


# Default keyworded only arguments
def func(a,b,*c,d,e="Rajiv"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,d="something",e="asdf")


# Optional keyworded only arguments
def func(**k):
    print(k)
func(name="Rajiv")


def func(a,b=1,*c,d,e="",**k):
    print(k)


# Anonymous function or lambda functions
sorted([4,2,1,5,3])
lambda a,b: a+b

(1,2)



a=1
b=2
c=print(a+b)
print(c)