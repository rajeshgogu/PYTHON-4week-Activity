# Take two comma separated input from the user and print length of user's name and print the number of count
# of characters input(Case insensitive) by user
name,char=input("Enter two comma separated values: ").split(",")
print(f"Length of {name} is {len(name.strip())}")

# "  Shivani  "  -------> "Shivani"  ------> "shivani"
# "  I  "  -------> "I" -------> "i"

print(f"{char} Character count is :{name.strip().lower().count(char.strip().lower())}")  # now name and Character both are in lower case 
# so we can easily count how many times character is present in name(case insensitive)