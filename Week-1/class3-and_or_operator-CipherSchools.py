# check two conditions at same time
# and , or

name = "abc"
age = 19

# And operator- Return True If all the conditions are satisfied.  
if name == "abc" and age == 19:
    print("Condition True")
else:
    print("Condition false")

if name == "abc" and age == 56:
    print("Condition True")
else:
    print("Condition false")

# Or operator- Return True If any one of the all condition is satisfied.
if name == "abc" or age == 19:
    print("Condition True")
else:
    print("Condition false")

if name == "adc" or age == 19:
    print("Condition True")
else:
    print("Condition false")
