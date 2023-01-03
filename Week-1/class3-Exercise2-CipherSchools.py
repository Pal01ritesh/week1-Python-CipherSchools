# Problem- Watch Coco
# Ask user's name and age
# if user's name start with ('a' or 'A') and age is above 10 then,
# print "you can watch coco movie"
# else print "sorry,you cann't watch coco movie"

user_name,age = input("Enter your comma separated name and age : ").split(",")
age=int(age)
if user_name[0]=='a' or user_name[0]=='A' and age>10:
    print("Yes, You can watch coco movie")
else:
    print("Sorry, You cann't watch coco movie")