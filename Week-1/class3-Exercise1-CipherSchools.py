# Problem- Number guessing game
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "You Win !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"

# Bonus- Google "How to generate random number in python" to generate random winnig number.

import random
winning_num = random.randint(0,100)
guess_num = int(input("Guess the number between 0 to 100 : "))
if winning_num == guess_num :
    print("You Win !!!!")
elif winning_num > guess_num:
    print("Too Low")
else:
    print("Too High")

print("Winning Number was :",winning_num)