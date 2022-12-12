# Tuple
a=[1,2,3]
a[0]=100
a[2]=200
print(a)

a=(1,2,3,4)
print(type(a))

a=5
b=9
a,b=b,a
c=a,b
type (c)
print(c)


def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d

c=sum_diff(10,5)
print(c)


a=(1,2,3,4)
list(range(5))
print(a)

tuple(range(5))


a=(1,2,3,4)
a=[1,2,3,4]
a.append(5)
a.append(7)
print(a)


# Dictionary

# key-->pair

# a=dict()
# a["name"]
# a[1]
# a[(1,2)]

a={
    "name":"Srikaran",
    1:"something",
    (1,2):"tuple key wat?"
    }

print(a["name"])
print(a[1])



a={
    "name":"Srikaran",
    "company":"Amazon",
    "college":"LPU"
}

key="marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exist")

key="marks"
print(a.get(key))


key="marks"
print(a.get(key,"key doesn't exist"))


for x in a.items():
    print(x)


for key,value in a.items():
    print(key,"-->",value)