# Exercise, Number Guessing Game
winning_number=7
num=int(input("Enter any number:"))
if num==winning_number:
    print("YOU WIN!!!")
elif num>winning_number:
    print("too high")
elif num<winning_number:
    print("too low")