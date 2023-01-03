# Problem- Ask user to input a number containig more than one digit 
# example - 1234
# Calculate- 1+2+3+4 and print

# Algorithm- 
# Ask input in string, i.e. doon't change string to int
# example- "1234"
# pick string character one by one and change to int 
# int(example[0]) + int(example[1]) + ........... go upto len(example)-1

n=input("Enter a number containing more than one digit : ")
total=0
i=0
while i < len(n):
    total+=int(n[i])
    i+=1
print(total)