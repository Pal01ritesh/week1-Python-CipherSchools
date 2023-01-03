# String methods part two-

#                          replace() method-
string = "she is beautiful and she is good dancer"
print(string.replace("is","was",1)) # we can also decide how many time we want to replace anything in the string.

#                          find() method-
print(string.find("is",7)) # we can also decide from where we want to start to find our required string.

# if we don't  know from where should we start then we can do;
is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)

#                          center() method-
name = "Shivam"

# output- **Shivam**
print(name.center(14,"*"))

name = input("Enter your name : ")
print(name.center(len(name)+8,"*"))

#                        Strings are immutable-
# This means strings cann't be changed once it created.

string = "string"

# string[1]='T'  - error

new_string = string.replace("t","T")
print(string)
print(new_string)

#                Use of assignment operator in string formatting

name = "Shiv"
# name = name + "am" 
name += "am"
print(name)

age = 19
age *= 2
print(age)