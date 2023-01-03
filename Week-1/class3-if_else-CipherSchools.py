# Syntax of else statment-

# we always use else statement a/f if statement.
# It is not necessary that else is use a/f every if statement but it is necesaary to have if statement b/f else statement to execute else statement.

age = input("Enter your age : ")
age = int(age)
if age >=14:
    print("You are eligible")
    print("You are above 14")
else:
    print("Sorry,Your are not eligible")

#                               In keyword :

name = "Shivam"
if "a" in name:
    print("Yes, a is present in",name)
else:
    print("No, a is not present in",name)
    