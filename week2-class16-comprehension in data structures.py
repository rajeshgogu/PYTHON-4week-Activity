# Comprehension

a=[]
for i in range(5):
    a.append(i)
print(a)


print([i for i in range(5)])

print(list(range(5)))

print(list(map(lambda x: x**2, range(5))))


a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)



n=5
[ [max(i+1,j+1,n-i,n-j) for j in range(n)]for i in range(n)]



print({i:i**2 for i in range(5)})