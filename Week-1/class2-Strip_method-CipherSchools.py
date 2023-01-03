name = "    Shi    vam   "
dots = "............."

# lstrip() method-  Return by removing all left side space given b/f word used in string.
print(name + dots)
print(name.lstrip() + dots)

# rstrip() method- RReturn by removing all right side space given a/f word used in string.
print(name.rstrip() + dots)

# strip() method- Return by removing both side space given b/f and a/f word used in string.
print(name.strip() + dots)

# replace() method- Return by removing both side space given b/f and a/f word used in string. As well as Remove space used in between word.
print(name.replace(" ","") + dots)

name,char = input("Enter your name and character that you wnat to count :").split(",")
print(len(name))
n=name.replace(" ","")
c=char.replace(" ","")
name_l=n.lower()
char_l=c.lower()
print(name_l.count(char_l))