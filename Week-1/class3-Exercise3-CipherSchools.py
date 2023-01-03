# Exercise One of Three
# Sum of n natural numbers
# ask user for a natural number (n)
# print total from 1 to n

n=int(input("Enter the number to get the sum : "))
i=1
t=0
while i<=n:
    t+=i
    i+=1
print(f"Sum of {n} natural numbers is {t}")