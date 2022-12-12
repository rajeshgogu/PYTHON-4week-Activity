# Other than 3 Data Types all the data types in python are immutable


a=[1,2,3,4]
print(a)


b=["Srikaran",1.5,1,print]
print(b)


print(len("Srikaran"))


print("Srikaran"+"D")


print([1,2,3]+[4,5,6])


a=[1,2,3,4,5]
for x in a:
    print(x)


print("z" in "Srikaran")

a=[1,2,3,4,5]
print(a[-1])


a=[1,2,3]
a.insert(1,100)
print(a)

a.append(5)
print(a)


a=[1,2,3,4]
a.pop()
print(a)


a=[1,2,3,4,5]
a.pop(2)
print(a)


a=["Srikaran","Sanjeev","shubham"]
a.remove("Rajiv")
print(a)


a=[4,2,4,5,6,8]
a.sort()
print(a)

b=[4,5,8,9,6,8,2]
print(sorted(b))

a=[1,2,3,4,5]
a.reverse()
print(a)

b=[1,2,3,4,5]
print(reversed(b))



# Map,Strip and split function

a=[1,2,3,4,]
# [1,4,9.16]
for x in map(lambda x:x**2,a):
    print(x)

int('1')
a=list(map(int,input().split()))
print(a)

print(type(a[0]))


print(",".join(["Srikaran","Sanjeev","Shubham"]))