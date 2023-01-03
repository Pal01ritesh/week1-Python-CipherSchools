# Int function

number_one = input("Enter first number ")
number_two = input("Enter second number ")
total = number_one + number_two  # It concate as string not add as integer
print("Total is " + total)
# total = '4' + '4' = '44'  

number_one = int(input("Enter first number "))
number_two = int(input("Enter second number "))
total = number_one + number_two
print("Total is " + str(total))

# str function- str()
# 4 ---> "4"

# int function- int()
# "4" ---> 4

# float function- float()
# "4" ---> 4.0

number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3) # Float