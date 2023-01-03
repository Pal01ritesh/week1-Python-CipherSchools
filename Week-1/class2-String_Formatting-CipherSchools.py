name = "Shivam"
age = 19
print("Hello " + name + " your age is " + str(age))  #ugly syntax

# String Formatting changes with python versions -
# pyhton 2 (very old type so we can skip it)
# python 3
# python 3.6 (best)

# python 3
print("Hello {} your age is {}".format(name,age)) # In Format function we need to think whether variable is string or integer.

# pyhton 3.6
print(f"Hello {name} your age is {age + 2}") # {} called placeholders
