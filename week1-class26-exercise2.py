# Ask user to input 3 numbers and you have to print average of three numbers using string formatting
# Take input in one line
a,b,c=int(input("Enter 1st,2nd,3rd number: ")).split()

average=(a+b+c)/3
print(f"Average of {a},{b},{c},is:",average)