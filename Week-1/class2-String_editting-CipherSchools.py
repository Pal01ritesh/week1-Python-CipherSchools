# String Indexing

language = "python"

# positions(index number)

# p=0 , -6
# y=1 , -5
# t=2 , -4
# h=3 , -3
# o=4 , -2
# n=5 , -1

print(language[3])
print(language[-6])

# String Slicing / selecting sub sequences

lang = "Mathematics"

# Syntax - [start argument : stop argument - 1]
print(lang[0:2])
print(lang[2:4])
print(lang[3:6])

print(lang[:]) # here default start argument is 0 and stop argumnet is last index +1
print(lang[:5])
print("Shivam" [1:4])

# Step Argument
# Syntax - [start argument : stop argument - 1 : step ]
print(lang[0:5:1])
print(lang[::2])
print("Shivam"[5::-1])