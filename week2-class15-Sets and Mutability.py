a={1,2,3,4}
print(type(a))

a.add(7)
a.remove(3)
a.add(2)
for i in a:
    print(i)


a={1,2,3,4}
b={3,4,5,6}

print(a-b)
print(a.union(b))
print(a.intersection(b))


a=[['']*3]*3
a[1][1]='x'
print(a)


a=[1,2,3,4,5]
print(id(a))


a=258
b=258
print(a==b)
print(a is b)



a="Srikaran"
hash(a)