# If we quotes inside same quotes it gives us error But if we use \" in place of " it don't give error. 

print("Hello \"World\" World")

# There are many espace squences like that-

# Single Quote escape sequences-
print('I\'m Shivam Singh')

# New Line escape sequences-
print("Line 1\nLine 2\nLine 3")

# Tab(big space) escape sequence-
print("name\tShivam")

# Backslash escape sequence-
print("This is \ Backslash") #this give us output but
#print("This is Backslash\")  
#this give syntax error b/c \" also have some special meaning. so, we cann't use \ just b/f ". To solve this we use Backslash Escape sequence-
print("This is Backslash\\")
# We have to use \\ to print \ , \\\\ to print \\ and so on.
print("This is Double Backslash\\\\")

# Backspace escape sequence-
print("Hell\blo")

