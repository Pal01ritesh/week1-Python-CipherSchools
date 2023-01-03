# Problem- Ask user to input 3 numbers and you have to print average of 3 numbers using string formatting.

# Bonus- try to take all three comma separated inputs in one line.

num1,num2,num3 = input("Enter three numbers ").split(",")
avg = (int(num1)+int(num2)+int(num3))/3
print(f"The Average of {(int(num1),int(num2),int(num3))} is {avg}")