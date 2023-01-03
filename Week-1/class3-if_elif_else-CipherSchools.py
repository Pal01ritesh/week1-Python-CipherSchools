# If elif else statement:

# Show ticket pricing:
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input(" Enter your age : "))

if 0<age<=3:
    print("Your ticket price : Free")
elif 3<age<=10:
    print("Your ticket price : 150")
elif 10<age<=60:
    print("Your ticket price : 250")
elif 60<age:
    print("Your ticket price : 200")
else:
    print("Invalid Input")