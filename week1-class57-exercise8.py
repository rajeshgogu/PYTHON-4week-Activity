# Calculate sum of digits of a number 
num=int(input("Enter a number: "))
s=str(num)
sum=0
for a in range(0,len(s)):
    sum+=int(s[a])
print("Sum of Digits of a number is:",sum)
